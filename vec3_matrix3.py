class Vec3():
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.values = [x, y, z]

    def mulc(self, c):
        """Element wise multiplication of vec3 by constant c
        Returns the result as a new vector"""
        new = []
        for i in range(len(self.values)):
            new.append(self.values[i] * c)
        return Vec3(new[0], new[1], new[2])




class Matrix3():
    def __init__(self, row1=None, row2=None, row3=None):
        if row1 is None: row1 = Vec3()
        if row2 is None: row2 = Vec3()
        if row3 is None: row3 = Vec3()
        self.m_values = [row1, row2, row3]
        
    def detA(self):
        """Returns the determinant of the matrix"""
        det =   self.m_values[0].values[0] * self.m_values[1].values[1] * self.m_values[2].values[2] + \
                self.m_values[0].values[1] * self.m_values[1].values[2] * self.m_values[2].values[0] + \
                self.m_values[0].values[2] * self.m_values[1].values[0] * self.m_values[2].values[1] - \
                self.m_values[0].values[2] * self.m_values[1].values[1] * self.m_values[2].values[0] - \
                self.m_values[0].values[1] * self.m_values[1].values[0] * self.m_values[2].values[2] - \
                self.m_values[0].values[0] * self.m_values[1].values[2] * self.m_values[2].values[1]
        return det

    def get_inverse(self):
        """Returns the inverse matrix of the matrix"""
        det = self.detA()

        inverse = Matrix3(Vec3(self.m_values[1].values[1] * self.m_values[2].values[2] - self.m_values[1].values[2] * self.m_values[2].values[1],
                               self.m_values[0].values[2] * self.m_values[2].values[1] - self.m_values[0].values[1] * self.m_values[2].values[2],
                               self.m_values[0].values[1] * self.m_values[1].values[2] - self.m_values[0].values[2] * self.m_values[1].values[1]).mulc(1 / det),
                          Vec3(self.m_values[1].values[2] * self.m_values[2].values[0] - self.m_values[1].values[0] * self.m_values[2].values[2],
                               self.m_values[0].values[0] * self.m_values[2].values[2] - self.m_values[0].values[2] * self.m_values[2].values[0],
                               self.m_values[0].values[2] * self.m_values[1].values[0] - self.m_values[0].values[0] * self.m_values[1].values[2]).mulc(1 / det),
                          Vec3(self.m_values[1].values[0] * self.m_values[2].values[1] - self.m_values[1].values[1] * self.m_values[2].values[0],
                               self.m_values[0].values[1] * self.m_values[2].values[0] - self.m_values[0].values[0] * self.m_values[2].values[1],
                               self.m_values[0].values[0] * self.m_values[1].values[1] - self.m_values[0].values[1] * self.m_values[1].values[0]).mulc(1 / det))
        return inverse
