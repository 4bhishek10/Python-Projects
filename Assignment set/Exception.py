
def find_average(mark_list):
    total = 0
    try:

        for i in range(0, len(mark_list)+1):
            total += mark_list1[i]
            marks_avg = total/len(mark_list)
        return marks_avg

    except ZeroDivisionError:
        print("ZeroDivisionError")

    except TypeError:
        print("TypeError")

    except NameError:
        print("TypeError")

    except ValueError:
        print("ValueError")
    except:
        print("some error occured in program")


m_list = ["1", 2, 3, 4]

try:
    mark1 = "A"
    mark1 = int("A")
    m_list = [mark1, 2, 3, 4]
    print("Average marks:", find_average(m_list))
except ZeroDivisionError:
    print("ZeroDivisionError")

except TypeError:
    print("TypeError")

except NameError:
    print("TypeError")

except ValueError:
    print("ValueError")
except:
    print("some error occured in program")
