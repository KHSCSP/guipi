import tkinter as tk

# define any functions
def get_pi():
    f = open("u11guipi/pi_short.txt", "r")  # open the file for reading
    pi = f.read() # read the data into one long string
    f.close() # close the file to release memory
    # TODO clean up
    pi = pi.replace("\n", "")

    return pi




# call the get_pi function
pi = get_pi()


# section 1 - setup main window



# section 2 - create frame1 - label_pi, label_instr, entry_bday, btn_go, label_ans



# 'raise' the frame you want visible first
# frame1.tkraise()
# root.mainloop()