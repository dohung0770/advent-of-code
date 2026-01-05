'''
--- Day 14: Reindeer Olympics ---
This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?




--- Part Two ---
Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.

Instead, at the end of each second, he awards one point to the reindeer currently in the lead. (If there are multiple reindeer tied for the lead, they each get one point.) He keeps the traditional 2503 second time limit, of course, as doing otherwise would be entirely ridiculous.

Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point. He stays in the lead until several seconds into Comet's second burst: after the 140th second, Comet pulls into the lead and gets his first point. Of course, since Dancer had been in the lead for the 139 seconds before that, he has accumulated 139 points by the 140th second.

After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312. So, with the new scoring system, Dancer would win (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points does the winning reindeer have?

'''


def parse_input(data: list[str]) -> list[tuple[str, int, int, int]]:
    output = []
    for line in data:
        p = line.split(' ')
        output.append((p[0], int(p[3]), int(p[6]), int(p[-2])))
        
    return output


def part1(race_time: int, reindeers: list[tuple[str, int, int, int]]):
    '''
    Find out which reindeer would win the race after 'race_time' seconds.
    Each reindeer can fly with 'fly_speed' for 'fly_duration' seconds,
    but has to rest 'rest_for' seconds before being able to fly again.

    Parameters:
        race_time (int): the duration of the race
        reindeers (list[tuple[str, int, int, int]]):
            = [reindeer name, fly_speed, fly_duration (in seconds), rest_for (in seconds)]
        
    Returns:
        int: the distance the winning reindeer has traveled
    '''

    max_dist = 0
    for name, fly_speed, fly_duration, rest_for in reindeers:
        fly_and_rest = race_time // (fly_duration + rest_for)
        rem = race_time % (fly_duration + rest_for)
        
        dist = fly_and_rest * fly_speed * fly_duration
        
        if rem > 0:
            dist += min(rem, fly_duration) * fly_speed
            
        print(f'{name} is at {dist}')
        max_dist = max(max_dist, dist)
        
    return max_dist


def part2(race_time: int, reindeers: list[tuple[str, int, int, int]]):
    '''
    Find out which reindeer would win the race after 'race_time' seconds with the new scoring system.
    That is at the end of each second, any reindeers who're at the lead, will gain one point each.
    Each reindeer can fly with 'fly_speed' for 'fly_duration' seconds,
    but has to rest 'rest_for' seconds before being able to fly again.

    Parameters:
        race_time (int): the duration of the race
        reindeers (list[tuple[str, int, int, int]]):
            = [reindeer name, fly_speed, fly_duration (in seconds), rest_for (in seconds)]
        
    Returns:
        int: the maximum points earned by the champion.
    '''

    n = len(reindeers)
    points = [0] * n
    dist = [0] * n
    fly_time = [0] * n
    rest_time = [0] * n

    for _ in range(race_time):
        leads = []
        max_dist = 0

        for i, (_, fly_speed, fly_duration, rest_for) in enumerate(reindeers):
            if rest_time[i] > 0:
                rest_time[i] -= 1
            elif fly_time[i] == 0:
                fly_time[i] = fly_duration

            if fly_time[i] > 0:
                fly_time[i] -= 1
                dist[i] += fly_speed
            
                if fly_time[i] == 0:
                    rest_time[i] = rest_for
                
            if max_dist < dist[i]:
                leads = [i]
                max_dist = dist[i]
            elif max_dist == dist[i]:
                leads.append(i)
                
        for idx in leads:
            points[idx] += 1
        
    print(points, dist)

    return max(points)


import os

if __name__ == '__main__':
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
        for line in file.readlines():
            data.append(line.strip())

    
    reindeers = parse_input(data)
    # print('part 1', part1(race_time=2503, reindeers=reindeers))
    print('part 2', part2(race_time=2503, reindeers=reindeers))
