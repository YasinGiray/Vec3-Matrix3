class Vec3():
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.values = [x, y, z]

    def mul(self, v):
        """Element wise multiplication of self by vector v
        Returns the result as a new vector"""
        new = []
        for i in range(len(self.values)):
            new.append(self.values[i] * v.values[i])
        return Vec3(new[0], new[1], new[2])

    def mulc(self, c):
        """Element wise multiplication of vec3 by constant c
        Returns the result as a new vector"""
        new = []
        for i in range(len(self.values)):
            new.append(self.values[i] * c)
        return Vec3(new[0], new[1], new[2])

    def add(self, v):
        """Element wise addition of vec3 by vector v
        Returns the result as a new vector"""
        new = []
        for i in range(len(self.values)):
            new.append(self.values[i] + v.values[i])
        return Vec3(new[0], new[1], new[2])

    def addc(self, c):
        """Element wise addition of vec3 by constant c
        Returns the result as a new vector"""
        new = []
        for i in range(len(self.values)):
            new.append(self.values[i] + c)
        return Vec3(new[0], new[1], new[2])

    def sub(self, v):
        """Element wise subtraction of vec3 by vector v
        Returns the result as a new vector"""
        new = []
        for i in range(len(self.values)):
            new.append(self.values[i] - v.values[i])
        return Vec3(new[0], new[1], new[2])

    def subc(self, c):
        """Element wise subtraction of vec3 by constant
        Returns the result as a new vector"""
        new = []
        for i in range(len(self.values)):
            new.append(self.values[i] - c)
        return Vec3(new[0], new[1], new[2])

    def cross(self, v):
        """Returns the cross product of self and vector v"""
        a = self.values
        new = [a[1] * v.values[2] - a[2] * v.values[1],
               a[2] * v.values[0] - a[0] * v.values[2],
               a[0] * v.values[1] - a[1] * v.values[0]]
        return Vec3(new[0], new[1], new[2])

    def dot(self, v):
        """Returns the dot product of self and vector v"""
        new = 0
        for i in range(len(self.values)):
            new += self.values[i] * v.values[i]
        return new

class Matrix3():
    def __init__(self, row1=None, row2=None, row3=None):
        if row1 is None: row1 = Vec3()
        if row2 is None: row2 = Vec3()
        if row3 is None: row3 = Vec3()
        self.m_values = [row1, row2, row3]

    def setIdentity(self):
        """Sets the current Matrix to an identity matrix
        self is an identity matrix after calling this method"""
        self.m_values[0] = Vec3(1, 0, 0)
        self.m_values[1] = Vec3(0, 1, 0)
        self.m_values[2] = Vec3(0, 0, 1)

    def mulV(self, vector):
        """Multiplication: Matrix times vector.
            'vector' is the vector with which to multiply.
            Return the result as a new Vec3.
            Make sure that you do not change self or the vector.
            return self * v"""
        new = []
        for i in range(len(self.m_values)):
            new.append(self.m_values[i].dot(vector))
        return Vec3(new[0], new[1], new[2])

    def roundM(self):
        """Rounds every entry in the matrix"""
        for i in range(len(self.m_values)):
            for j in range(len(self.m_values[i].values)):
                self.m_values[i].values[j] = round(self.m_values[i].values[j])

    def mulM(self, m):
        """Multiplication: Matrix times Matrix.
            m is the matrix with which to multiply.
            Return the result as a new Matrix3.
            Make sure that you do not change self or the other matrix.
            return this * m"""
        new = []
        tmp = [[], [], []]
        for row in m.m_values:
            tmp[0].append(row.values[0])
            tmp[1].append(row.values[1])
            tmp[2].append(row.values[2])

        for i in range(len(self.m_values)):
            item = Vec3(tmp[i][0], tmp[i][1], tmp[i][2])
            new.append(self.mulV(item))

        trans = [[], [], []]
        for i in new:
            trans[0].append(i.values[0])
            trans[1].append(i.values[1])
            trans[2].append(i.values[2])

        result = []
        for i in range(len(trans)):
            result.append(Vec3(trans[i][0], trans[i][1], trans[i][2]))

        return Matrix3(result[0], result[1], result[2])

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
