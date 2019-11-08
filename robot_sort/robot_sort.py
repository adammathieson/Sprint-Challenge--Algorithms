import time

class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"


    # def sort_right(self):
    #     while self.move_right():
    #         print("Moving to---->", self._position)
    #         if self.compare_item() == 1:
    #             print(f'swap {self._item}')
    #             self.swap_item()
    #             print(f'for {self._item} at postition {self._position}')
    #             # time.sleep(1)
    #         else:
    #             next

    #         # elif self.compare_item() == None and self.move_right() == False:
    #         #     return
                
    #     print("<<Call sort left<<", self._list)
    #     return self.sort_left()

    # def sort_left(self):
    #     print(f"+++++++{self._list[self._position]}++++++++++")
    #     if self._list[self._position] == None:
    #         self.swap_item()
    #         return
    #     else:
    #         while self.move_left() and self._item != None:
    #             print(f"{self._position}<-----")
                
    #             if self.compare_item() == None:
    #                 print(f"swap {self._item}")
    #                 self.swap_item()
    #                 print(f"for {self._item} at position {self._position}")
    #                 break
    #             # elif self.compare_item() == None and self.move_right() == False:
    #             #     self.swap_item() 
    #             #     return

    #         print("--> moving right")
    #         self.move_right()
    #         print(f"swap {self._item}")
    #         self.swap_item()
    #         print(f"for {self._item} at position {self._position}")
            
    #         # time.sleep(1)
    #             # elif self._item == None:
    #                 # break
                    
    #             # if self.move_right() == False:
    #             #     return
    #             # else:
    #             #     next
            
    #         print(">>Call sort right>>", self._list)
    #         return self.sort_right()
            # return 'Sorted'

# [6, 7, 1, -4, 12] # len = 5 after start [None, 7, 1, -4, 12] item is 6, sort list to the right and return
# to 0 index and to swap for low value when finished
    # def sort(self):

    #     # self.set_light_on()
    #     print("START HERE")
    #     self.swap_item()
    #     print(f"Initial swap - (6): {self._item} ")

    #     self.sort_right()
            
    #     print(f"Congratulations! Your list has been sorted: {self._list}")
    #     return self._list
            
        # if self.move_right():
        #     self.sort_right()
        # elif self.move_right() == False:
            
        
    # print(l, self._item, self.light_is_on(), self._position)
            


        #     print("---->", self._position)
        #     if self.compare_item() == 1:
        #         print(self.compare_item(), self._item, self._list[self._position])
        #         print(f'swapping {self._item} value at {self._position} position')
        #         self.swap_item()
        #         print(f'for {self._item} value')

                
        




        # count = len(l) - 2
        # print("Starting Count:", count)

        # self.swap_item()
        # self.move_to_start()

        # # def start(self, count):
        # while count > 0:
        #     # self.compare_item()
        #     if self.compare_item() == -1 and self.move_right() == True:
        #         print(f'swapping {self._item} value at {self._position} position')
        #         self.swap_item()
        #         print(f'for {self._item} value at {self._position} position')
        #         self.move_right()
        #         time.sleep(1)

        #     elif self.compare_item() == -1 and self.move_right() == False:
        #         print(f'swapping {self._item} value at {self._position} position')
        #         self.swap_item()
        #         print(f'for {self._item} value at {self._position} position')
        #         self.move_to_start()
        #         count = len(l) -2
        #         print('count', count)
        #         time.sleep(1)

        #     elif self.compare_item() != -1 and self.move_right() == True:
        #         print(f'no swap at: {self._position} position')
        #         print("item: ", self._item)
        #         self.move_right()
        #         count -= 1
        #         print('count', count)
        #         time.sleep(1)

        #     elif self.compare_item() != -1 and self.move_right() == False:
        #         print(f'no swap at: {self._position} position')
        #         print("item: ", self._item)
        #         self.move_to_start()
        #         count = len(l) - 2
        #         print('count', count)
        #         time.sleep(1)

        #     # else:
        #     #     # self.swap_item()
        #     #     self.move_to_start()
        #     #     count = len(l) -2
        #     #     print(f'return to start, reset count to {count}')

        # # self.move_to_start()
        # # self.can_move_left()
        # # self.swap_item()

        # return "List is sorted"


    def sort_right(self):
        while self.move_right():
            if self.compare_item() == 1:
                self.swap_item()

        return self.sort_left()

    def sort_left(self):
        if self._list[self._position] == None:
            self.swap_item()
            return
        else:
            while self.move_left() and self._item != None:
                if self.compare_item() == None:
                    self.swap_item()
                    break
            self.move_right()
            self.swap_item()
            return self.sort_right()

    def sort(self):
        self.swap_item()
        self.sort_right()
            
        # print(f"Congratulations! Your list has been sorted: {self._list}")
        return self._list       

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    # l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]
    l = [6, 7, 1, -4, 12]
    robot = SortingRobot(l)

    robot.sort()
    # robot.swap_item()

    # print("held item: ", robot._item)
    # print("current position: ", robot._position)
    # print(robot._list)