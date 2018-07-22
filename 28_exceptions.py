while True:
    try:
        num = int(input("provide a number plz\n"))
        print(18 / num)
        # what if I need the exact value -> print(18. / num)
        break
    except ValueError:
        print("Something wrong")
    except NameError:
        print("Something wrong")
    except ZeroDivisionError:
        print("Something wrong")
    except:
        break
    finally:
        print("see you later")