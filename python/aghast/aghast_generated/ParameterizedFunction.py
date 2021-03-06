# automatically generated by the FlatBuffers compiler, do not modify

# namespace: aghast_generated

import flatbuffers


class ParameterizedFunction(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAsParameterizedFunction(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ParameterizedFunction()
        x.Init(buf, n + offset)
        return x

    # ParameterizedFunction
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ParameterizedFunction
    def Expression(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ParameterizedFunction
    def Parameters(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Parameter import Parameter

            obj = Parameter()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ParameterizedFunction
    def ParametersLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ParameterizedFunction
    def Paramaxis(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Int32Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4),
            )
        return 0

    # ParameterizedFunction
    def ParamaxisAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # ParameterizedFunction
    def ParamaxisLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ParameterizedFunction
    def ParameterCovariances(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Covariance import Covariance

            obj = Covariance()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ParameterizedFunction
    def ParameterCovariancesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0


def ParameterizedFunctionStart(builder):
    builder.StartObject(4)


def ParameterizedFunctionAddExpression(builder, expression):
    builder.PrependUOffsetTRelativeSlot(
        0, flatbuffers.number_types.UOffsetTFlags.py_type(expression), 0
    )


def ParameterizedFunctionAddParameters(builder, parameters):
    builder.PrependUOffsetTRelativeSlot(
        1, flatbuffers.number_types.UOffsetTFlags.py_type(parameters), 0
    )


def ParameterizedFunctionStartParametersVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)


def ParameterizedFunctionAddParamaxis(builder, paramaxis):
    builder.PrependUOffsetTRelativeSlot(
        2, flatbuffers.number_types.UOffsetTFlags.py_type(paramaxis), 0
    )


def ParameterizedFunctionStartParamaxisVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)


def ParameterizedFunctionAddParameterCovariances(builder, parameterCovariances):
    builder.PrependUOffsetTRelativeSlot(
        3, flatbuffers.number_types.UOffsetTFlags.py_type(parameterCovariances), 0
    )


def ParameterizedFunctionStartParameterCovariancesVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)


def ParameterizedFunctionEnd(builder):
    return builder.EndObject()
