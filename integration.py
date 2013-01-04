
# Settings
endTime = 10
dt = 1
t = dt

acceleration = 10

# Values
class State:
    x = 0
    v = 0
    
    def __add__( self, other ):
        new = State()
        new.x = self.x + other.x
        new.v = self.v + other.v
        return new
    
    def __mul__( self, scalar ):
        new = State()
        new.x = self.x * scalar
        new.v = self.v * scalar
        return new

# Euler
def euler( state, derivative, dt ):
    new = state + derivative * dt
    newDerivative = State()
    newDerivative.x = new.v # Derivative of position is velocity.
    newDerivative.v = derivative.v
    return new, newDerivative

# Improved Euler
def eulerImproved( state, derivative, dt ):
    bad, badDerivative = euler( state, derivative, dt )
    new = state + (derivative + badDerivative) * (dt / 2)
    newDerivative = State()
    newDerivative.x = new.v # Derivative of position is velocity.
    newDerivative.v = derivative.v
    return new, newDerivative

# RK4
def accelerate( state, t ):
    global acceleration
    return acceleration # Directly return acceleration cause it stays constant.

def evaluate( initial, t, dt, derivative ):
    state = State()
    state.x = initial.x + derivative.x * dt
    state.v = initial.v + derivative.v * dt
    
    newDerivative = State()
    newDerivative.x = state.v # Derivative of position is velocity.
    newDerivative.v = accelerate( state, t + dt )
    return newDerivative
    
def rk4( state, t, dt ):
    a = evaluate( state, t, 0, State() )
    b = evaluate( state, t, dt * 0.5, a )
    c = evaluate( state, t, dt * 0.5, b )
    d = evaluate( state, t, dt, c )
    
    dxdt = 1 / 6 * (a.x + 2 * (b.x + c.x) + d.x)
    dvdt = 1 / 6 * (a.v + 2 * (b.v + c.v) + d.v)
    
    new = State()
    new.x = state.x + dxdt * dt
    new.v = state.v + dvdt * dt
    return new, dxdt, dvdt

# Test
start = State()
target = 0.5 * acceleration * (endTime * endTime) # s = 1/2 a t^2

eulerState = start
eulerDerivative = State()
eulerDerivative.v = acceleration # Derivative of velocity is acceleration.

eulerImpState = start
eulerImpDerivative = State()
eulerImpDerivative.v = acceleration # Derivative of velocity is acceleration.

rk4State = start

quit = False
while quit == False:
    # Euler
    eulerState, eulerDerivative = euler( eulerState, eulerDerivative, dt )
    
    # Improved Euler
    eulerImpState, eulerImpDerivative = eulerImproved( eulerImpState, eulerImpDerivative, dt )
    
    # RK4
    rk4State, dxdt, dvdt = rk4( rk4State, t, dt )
    
    # Show result
    print( 'Time: %.2f' % (t) )
    print( '   Euler: x = %.2f, v = %.2f, dx = %.2f, dv = %.2f, diffTarget = %.2f' % 
           (eulerState.x, eulerState.v, eulerDerivative.x, eulerDerivative.v, target - eulerState.x) )
    print( '   Euler Improved: x = %.2f, v = %.2f, dx = %.2f, dv = %.2f, diffTarget = %.2f' % 
           (eulerImpState.x, eulerImpState.v, eulerImpDerivative.x, eulerImpDerivative.v, target - eulerImpState.x) )
    print( '   Rk4: x = %.2f, v = %.2f, dxdt = %.2f, dvdt = %.2f, diffTarget = %.2f' % 
           (rk4State.x, rk4State.v, dxdt, dvdt, target - rk4State.x) )
    print()
    
    # Next step
    t += dt
    quit = (t >= (endTime + 0.00001))