import numpy as np
from Connect import Connect
import threading

class Formasyon():


   Connect = Connect()




   def triangle(self):

      Kp = np.array([1, 1, 1])
      Kd = np.array([1, 1, 1])

      P = Connect.Positions

      Distance = np.array([1,0,1])

      Arr1 = np.array([0, 0, 0])
      Arr2 = np.array([0, 0, 0])
      Arr3 = np.array([0, 0, 0])



      # Formasyon Agent1
      def Agent1():


         for j in range(3):
            if P[0] == P[j]:
               continue

            Ar = Kp * (P[j] - P[0] - Distance[0])
            Arr1 = Ar + Arr1

      # Formasyon Agent2
      def Agent2():

         global Arr2

         for j in range(3):
            if P[1] == P[j]:
               continue

            Ar = Kp * (P[j] - P[0] - Distance[0])
            Arr2 = Ar + Arr2

      # Formasyon Agent3

      def Agent3():

         global Arr3

         for j in range(3):
            if P[2] == P[j]:
               continue

            Ar = Kp * (P[j] - P[0] - Distance[0])
            Arr3 = Ar + Arr3

      t1 = threading.Thread(target=Agent1())
      t2 = threading.Thread(target=Agent2())
      t3 = threading.Thread(target=Agent3())

      t1.start()
      t2.start()
      t3.start()


      Agents = Connect.Agents

      location1 = P[0] - Arr1
      location2 = P[1] - Arr2
      location3 = P[2] - Arr3


      while ((location2-location1 ) != Distance[0]) and ((location3-location2) != Distance[0] and ((location3-location1) != Distance[0])):
            vehicle1 = Agents[0]
            # Dronun belirli bir noktaya gitmesi için komut gönderme
            vehicle1.simple_goto(P[0])

            # Dronun hareket etmesini bekleme
            while True:
               current_position = vehicle1.location.global_relative_frame
               if current_position.lat == P[0].lat and current_position.lon == P[0].lon:
                  print("Reached target position")
                  break

            vehicle2 = Agents[1]
            # Dronun belirli bir noktaya gitmesi için komut gönderme
            vehicle2.simple_goto(P[1])

            # Dronun hareket etmesini bekleme
            while True:
               current_position = vehicle2.location.global_relative_frame
               if current_position.lat == P[1].lat and current_position.lon == P[1].lon:
                  print("Reached target position")
                  break

            vehicle3 = Agents[2]
            # Dronun belirli bir noktaya gitmesi için komut gönderme
            vehicle3.simple_goto(P[2])

            # Dronun hareket etmesini bekleme
            while True:
               current_position = vehicle3.location.global_relative_frame
               if current_position.lat == P[2].lat and current_position.lon == P[2].lon:
                  print("Reached target position")
                  break
