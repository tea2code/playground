import math
import time

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
    
def render( state ):
    print( 'State (', round(state.x, 4), ',', round(state.v, 4), ')' )
    
def hires_time_in_seconds():
    return time.perf_counter()
    
t = 0.0
dt = 1/ 60
currentTime = hires_time_in_seconds()
accumulator = 0.0

previous = State( 100, 0 )
current = previous

while math.fabs(current.x) > 1 or math.fabs(current.v) > 1:
    newTime = hires_time_in_seconds()
    frameTime = min( newTime - currentTime, 0.25 )
    currentTime = newTime
    
    accumulator += frameTime

    while accumulator >= dt:
        print( 'Accumulator =', '%.10f' % accumulator, 's' )
        previous = current
        current = integrate( current, t, dt )
        accumulator -= dt
        t += dt

    alpha = accumulator / dt
    print( 'Alpha =', round(alpha, 5) )
    x = current.x * alpha + previous.x * (1 - alpha)
    v = current.v * alpha + previous.v * (1 - alpha)
    state = State( x, v )
    render( state )
    time.sleep( 0.03 ) # Simulate high load.