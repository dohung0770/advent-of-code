from main import part1

def test_part1():
    data = [
        'p=0,4 v=3,-3',
        'p=6,3 v=-1,-3',
        'p=10,3 v=-1,2',
        'p=2,0 v=2,-1',
        'p=0,0 v=1,3',
        'p=3,0 v=-2,-2',
        'p=7,6 v=-1,-3',
        'p=3,0 v=-1,-2',
        'p=9,3 v=2,3',
        'p=7,3 v=-1,2',
        'p=2,4 v=2,-3',
        'p=9,5 v=-3,-3'
    ]
    
    robots = []
    velocity = []

    # Preprocess data
    for line in data:
        left, right = line.split(' ')
        robots.append([int(v) for v in left[2:].split(',')])
        velocity.append([int(v) for v in right[2:].split(',')])
  
    assert part1(11, 7, robots, velocity, t=100) == 12
