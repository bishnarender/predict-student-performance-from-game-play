#!/usr/bin/env python
# coding: utf-8

# In[ ]:

@cc.export('fqids_to_number', 'i8[::1](u4[:, ::1])')
@numba.jit(nopython=True, nogil=True)
def fqids_to_number(data):

  n = data.shape[0]
  out = np.full(n, 129, dtype=np.int64)

  for i in range(n):

    v = data[i]

    if v[0] == 0:
      out[i] = 0
    elif v[0] == 97:
      if v[9] == 0:
        out[i] = 1
      elif v[9] == 95:
        out[i] = 2
    elif v[0] == 98:
      if v[1] == 108:
        if v[5] == 0:
          out[i] = 3
        elif v[5] == 95:
          if v[6] == 48:
            out[i] = 4
          elif v[6] == 49:
            out[i] = 5
          elif v[6] == 98:
            if v[11] == 0:
              out[i] = 6
            elif v[11] == 95:
              out[i] = 7
          elif v[6] == 109:
            out[i] = 8
          elif v[6] == 110:
            out[i] = 9
          elif v[6] == 116:
            if v[8] == 99:
              out[i] = 10
            elif v[8] == 109:
              if v[11] == 49:
                out[i] = 11
              elif v[11] == 50:
                out[i] = 12
      elif v[1] == 111:
        out[i] = 13
      elif v[1] == 117:
        if v[13] == 0:
          out[i] = 14
        elif v[13] == 46:
          if v[19] == 48:
            out[i] = 15
          elif v[19] == 49:
            out[i] = 16
          elif v[19] == 98:
            if v[25] == 98:
              out[i] = 17
            elif v[25] == 110:
              out[i] = 18
    elif v[0] == 99:
      if v[1] == 104:
        if v[2] == 51:
          out[i] = 19
        elif v[2] == 97:
          if v[4] == 49:
            if v[12] == 0:
              out[i] = 20
            elif v[12] == 95:
              out[i] = 21
          elif v[4] == 50:
            if v[12] == 0:
              out[i] = 22
            elif v[12] == 95:
              out[i] = 23
          elif v[4] == 52:
            out[i] = 24
      elif v[1] == 111:
        if v[2] == 102:
          out[i] = 25
        elif v[2] == 108:
          out[i] = 26
        elif v[2] == 110:
          out[i] = 27
      elif v[1] == 114:
        out[i] = 28
      elif v[1] == 115:
        out[i] = 29
    elif v[0] == 100:
      if v[1] == 105:
        if v[9] == 0:
          out[i] = 30
        elif v[9] == 46:
          out[i] = 31
      elif v[1] == 111:
        if v[4] == 95:
          if v[11] == 99:
            out[i] = 32
          elif v[11] == 116:
            out[i] = 33
        elif v[4] == 98:
          out[i] = 34
    elif v[0] == 101:
      out[i] = 35
    elif v[0] == 102:
      if v[1] == 108:
        out[i] = 36
      elif v[1] == 111:
        out[i] = 37
    elif v[0] == 103:
      if v[1] == 108:
        out[i] = 38
      elif v[1] == 114:
        if v[2] == 97:
          out[i] = 39
        elif v[2] == 111:
          if v[10] == 0:
            out[i] = 40
          elif v[10] == 95:
            out[i] = 41
    elif v[0] == 105:
      out[i] = 42
    elif v[0] == 106:
      if v[1] == 97:
        out[i] = 43
      elif v[1] == 111:
        if v[8] == 0:
          out[i] = 44
        elif v[8] == 46:
          if v[9] == 104:
            out[i] = 45
          elif v[9] == 112:
            if v[13] == 48:
              out[i] = 46
            elif v[13] == 49:
              out[i] = 47
            elif v[13] == 50:
              if v[15] == 98:
                out[i] = 48
              elif v[15] == 110:
                out[i] = 49
        elif v[8] == 95:
          if v[13] == 0:
            out[i] = 50
          elif v[13] == 46:
            if v[14] == 104:
              if v[24] == 0:
                out[i] = 51
              elif v[24] == 95:
                out[i] = 52
            elif v[14] == 112:
              if v[18] == 48:
                if v[19] == 46:
                  if v[20] == 98:
                    out[i] = 53
                  elif v[20] == 110:
                    out[i] = 54
                elif v[19] == 95:
                  out[i] = 55
              elif v[18] == 49:
                if v[19] == 46:
                  if v[20] == 98:
                    out[i] = 56
                  elif v[20] == 110:
                    out[i] = 57
                elif v[19] == 95:
                  out[i] = 58
              elif v[18] == 50:
                if v[19] == 46:
                  if v[20] == 98:
                    out[i] = 59
                  elif v[20] == 110:
                    out[i] = 60
                elif v[19] == 95:
                  out[i] = 61
    elif v[0] == 107:
      out[i] = 62
    elif v[0] == 108:
      if v[2] == 99:
        out[i] = 63
      elif v[2] == 103:
        if v[7] == 0:
          out[i] = 64
        elif v[7] == 46:
          out[i] = 65
    elif v[0] == 109:
      out[i] = 66
    elif v[0] == 110:
      if v[1] == 101:
        out[i] = 67
      elif v[1] == 111:
        out[i] = 68
    elif v[0] == 111:
      out[i] = 69
    elif v[0] == 112:
      if v[1] == 104:
        out[i] = 70
      elif v[1] == 108:
        if v[6] == 0:
          out[i] = 71
        elif v[6] == 46:
          out[i] = 72
    elif v[0] == 114:
      if v[2] == 97:
        if v[6] == 0:
          out[i] = 73
        elif v[6] == 46:
          if v[12] == 48:
            if v[14] == 110:
              out[i] = 74
            elif v[14] == 112:
              out[i] = 75
          elif v[12] == 49:
            if v[14] == 110:
              out[i] = 76
            elif v[14] == 112:
              out[i] = 77
          elif v[12] == 50:
            if v[14] == 98:
              out[i] = 78
            elif v[14] == 110:
              out[i] = 79
            elif v[14] == 112:
              out[i] = 80
        elif v[6] == 95:
          if v[11] == 0:
            out[i] = 81
          elif v[11] == 46:
            if v[17] == 48:
              if v[19] == 110:
                out[i] = 82
              elif v[19] == 112:
                out[i] = 83
            elif v[17] == 49:
              if v[19] == 110:
                out[i] = 84
              elif v[19] == 112:
                out[i] = 85
            elif v[17] == 50:
              if v[19] == 98:
                out[i] = 86
              elif v[19] == 110:
                out[i] = 87
              elif v[19] == 112:
                out[i] = 88
      elif v[2] == 109:
        out[i] = 89
      elif v[2] == 112:
        out[i] = 90
      elif v[2] == 116:
        out[i] = 91
    elif v[0] == 115:
      if v[1] == 97:
        out[i] = 92
      elif v[1] == 101:
        out[i] = 93
    elif v[0] == 116:
      if v[1] == 101:
        out[i] = 94
      elif v[1] == 111:
        if v[2] == 98:
          out[i] = 95
        elif v[2] == 99:
          if v[3] == 97:
            out[i] = 96
          elif v[3] == 108:
            if v[8] == 0:
              out[i] = 97
            elif v[8] == 95:
              out[i] = 98
          elif v[3] == 111:
            if v[12] == 0:
              out[i] = 99
            elif v[12] == 102:
              out[i] = 100
        elif v[2] == 101:
          out[i] = 101
        elif v[2] == 102:
          out[i] = 102
        elif v[2] == 103:
          out[i] = 103
        elif v[2] == 104:
          out[i] = 104
        elif v[2] == 109:
          if v[3] == 97:
            out[i] = 105
          elif v[3] == 105:
            out[i] = 106
        elif v[2] == 115:
          out[i] = 107
      elif v[1] == 114:
        if v[2] == 97:
          if v[6] == 0:
            out[i] = 108
          elif v[6] == 46:
            out[i] = 109
        elif v[2] == 105:
          if v[8] == 99:
            out[i] = 110
          elif v[8] == 115:
            out[i] = 111
      elif v[1] == 117:
        if v[5] == 0:
          out[i] = 112
        elif v[5] == 46:
          if v[6] == 99:
            if v[14] == 48:
              out[i] = 113
            elif v[14] == 49:
              out[i] = 114
            elif v[14] == 50:
              out[i] = 115
          elif v[6] == 100:
            out[i] = 116
          elif v[6] == 102:
            out[i] = 117
          elif v[6] == 104:
            if v[7] == 105:
              out[i] = 118
            elif v[7] == 117:
              if v[8] == 98:
                out[i] = 119
              elif v[8] == 109:
                out[i] = 120
          elif v[6] == 107:
            out[i] = 121
          elif v[6] == 108:
            out[i] = 122
          elif v[6] == 119:
            out[i] = 123
    elif v[0] == 117:
      out[i] = 124
    elif v[0] == 119:
      if v[1] == 101:
        if v[5] == 0:
          out[i] = 125
        elif v[5] == 98:
          out[i] = 126
      elif v[1] == 104:
        out[i] = 127
      elif v[1] == 111:
        out[i] = 128
  return out