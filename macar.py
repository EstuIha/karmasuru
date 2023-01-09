from scipy.optimize import linear_sum_assignment
import numpy as np


class Macar_algorithm():



    def matches(self,points1,points2):


      # iki grup nokta arasındaki uzaklıkları hesaplayın
      distances = np.sqrt(np.sum((points1[:, np.newaxis, :] - points2[np.newaxis, :, :]) ** 2, axis=-1))

      # Macar algoritmasını uygulanması ve eşleşme
      row_ind, col_ind = linear_sum_assignment(distances)
      global pozition
      pozition = list()

      global target_pozition
      target_pozition = list()

      for i in range(len(row_ind)):
        pozition.append(row_ind[i])
      for i in range(len(col_ind)):
        target_pozition.append(col_ind[i])

