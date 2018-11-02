#!/usr/bin/env python

import struct

import numpy
import flatbuffers

import histos.histos_generated
import histos.histos_generated.Book

import histos.checktype

class Book(object):
    def tobuffer(self, internalize=False):
        builder = flatbuffers.Builder(1024)
        builder.Finish(self._toflatbuffers(builder, internalize, None))
        return builder.Output()

    @classmethod
    def frombuffer(cls, buffer, offset=0):
        out = cls.__new__(cls)
        out._flatbuffers = histos.histos_generated.Book.Book.GetRootAsBook(buffer, offset)
        return out

    def toarray(self):
        return numpy.frombuffer(self.tobuffer(), dtype=numpy.uint8)

    @classmethod
    def fromarray(cls, array):
        return cls.frombuffer(array)

    def tofile(self, file, internalize=False):
        opened = False
        if not hasattr(file, "write"):
            file = open(file, "wb")
            opened = True

        if not hasattr(file, "tell"):
            class FileLike(object):
                def __init__(self, file):
                    self.file = file
                    self.offset = 0
                def write(self, data):
                    self.file.write(data)
                    self.offset += len(data)
                def close(self):
                    try:
                        self.file.close()
                    except:
                        pass
                def tell(self):
                    return self.offset
            file = FileLike(file)

        try:
            file.write(b"hist")
            builder = flatbuffers.Builder(1024)
            builder.Finish(self._toflatbuffers(builder, False, file))
            offset = file.tell()
            file.write(builder.Output())
            file.write(struct.pack("<Q", offset))
            file.write(b"hist")

        finally:
            if opened:
                file.close()

    @classmethod
    def fromfile(cls, file, mode="r+"):
        if isinstance(file, str):
            file = numpy.memmap(file, dtype=numpy.uint8, mode=mode)
        if file[:4].tostring() != b"hist":
            raise OSError("file does not begin with magic 'hist'")
        if file[-4:].tostring() != b"hist":
            raise OSError("file does not end with magic 'hist'")
        offset, = struct.unpack("<Q", file[-12:-4])
        return cls.frombuffer(file[offset:-12])

    def __init__(self, identifier, title=""):
        self.identifier = identifier
        self.title = title
    
    @property
    def identifier(self):
        if not hasattr(self, "_identifier"):
            self._identifier = self._flatbuffers.Identifier()
        return self._identifier

    @identifier.setter
    def identifier(self, value):
        self._identifier = histos.checktype.string("Book.identifier", value)

    @property
    def title(self):
        if not hasattr(self, "_title"):
            self._title = self._flatbuffers.Title()
        return self._title

    @title.setter
    def title(self, value):
        self._title = histos.checktype.string("Book.title", value)

    def _valid(self):
        pass

    def __repr__(self):
        return "<{0} {1} at 0x{2:012x}>".format(type(self).__name__, repr(self.identifier), id(self))

    def _toflatbuffers(self, builder, internalize, file):
        self._valid()

        identifier = builder.CreateString(self._identifier)
        if len(self._title) > 0:
            title = builder.CreateString(self._title)
        histos.histos_generated.Book.BookStart(builder)
        histos.histos_generated.Book.BookAddIdentifier(builder, identifier)
        if len(self._title) > 0:
            histos.histos_generated.Book.BookAddTitle(builder, title)
        return histos.histos_generated.Book.BookEnd(builder)
