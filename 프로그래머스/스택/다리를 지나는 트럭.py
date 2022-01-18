class Truck :
    def __init__(self, weight):
        self.weight = weight
        self.time =0
        

def solution(bridge_length, weight, truck_weights):
    bridge = list()
    result_queue = []
    result_case_number = len(truck_weights)
    seconds = 0
    current_weight = 0
    while True:
        if bridge and bridge[0].time == bridge_length:
            out_truck = bridge.pop(0)
            result_queue.append( out_truck )
            current_weight -= out_truck.weight
        else :
            pass 
        if truck_weights and current_weight+ truck_weights[0]  <= weight:   
            enter_truck = Truck(truck_weights.pop(0))
            bridge.append(enter_truck)
            current_weight += enter_truck.weight
        else :
            pass
        for truck_bridge in bridge :
            truck_bridge.time += 1
        seconds += 1
        if len(result_queue) == result_case_number :
            break
        
    return seconds