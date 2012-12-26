import math

class State:
    def __init__( self, x, v ):
        self.x = x
        self.v = v

class Derivative:
    def __init__( self, dx, dv ):
        self.dx = dx
        self.dv = dv

def acceleration( state, t ):
    k = 10
    b = 1
    return -k * state.x - b * state.v
        
def evaluate( initial, t, dt, d ):
    x = initial.x + d.dx * dt
    v = initial.v + d.dv * dt
    state = State( x, v )
    
    dx = state.v
    dv = acceleration( state, t + dt )
    output = Derivative( dx, dv )
    return output
    
def integrate( state, t, dt ):
    a = evaluate( state, t, 0, Derivative(0, 0) )
    b = evaluate( state, t, dt * 0.5, a )
    c = evaluate( state, t, dt * 0.5, b )
    d = evaluate( state, t, dt, c )
    
    dxdt = 1 / 6 * (a.dx + 2 * (b.dx + c.dx) + d.dx)
    dvdt = 1 / 6 * (a.dv + 2 * (b.dv + c.dv) + d.dv)
    
    state.x = state.x + dxdt * dt
    state.v = state.v + dvdt * dt
    return state
    
state = State( 100, 0 )

t = 0
dt = 0.1

while math.fabs(state.x) > 0.001 or math.fabs(state.v) > 0.001:
    print( round(state.x, 2), ", ", round(state.v, 2) )
    state = integrate( state, t, dt )
    t += dt