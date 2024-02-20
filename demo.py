from tkinter import *
from tkinter import ttk
from PIL import ImageTk , Image
import os
import pass_to_hash
from connect import *
import cv2 as cv
import face_recognition
from winsound import Beep
import messaging
import weapon_detect
import smoke_fire
import time

class Thesis_Project:
    """ Initializing variables and login interface """

    def __init__(self, interface):

        self.interface = interface
        self.interface.geometry("1080x600")
        self.interface.title('''An Intensive Research on application of machine learning techniques to improve the Physical
                                Security in Banking Environment using Surveillance System.''')
        self.interface.resizable(False, False)
        self.interface.config(bg="lightgrey")

        self.ret = False
        self.file = "haarcascade_frontalface_default.xml"
        self.data = cv.CascadeClassifier(self.file)

        # creating left_frame
        self.frame_image = Frame(self.interface, width=650, height=270, bg='lightgray')
        self.frame_image.grid(row=0, column=0, padx=8, pady=5)

        # loading images in frame2_right###
        self.bg = Image.open("banking_solution_img4.png")
        # resized image
        self.resized = self.bg.resize((680, 590), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(self.resized)

        # Image size
        self.bg_image = Label(self.frame_image, image=self.image2)
        self.bg_image.pack(pady=1)

        # creating right_frame
        self.frame_right = Frame(self.interface, width=300, height=400, bg='lightgreen')
        self.frame_right.grid(row=0, column=1, padx=8, pady=5)


        self.desc = Label(self.frame_right, text="Login to Use the Prototype", font=("Goudy old sytly", 10, "bold"),
                          fg="red")
        self.desc.place(x=10, y=10)

        #button
        self.btn_login= Button(self.frame_right,text="Login here !!!",fg="black",font="serif 12 bold", command=self.login_here)
        self.btn_login.place(x=100, y=90)

        self.btn_register = Button(self.frame_right, text="Register here !!",command=self.register_here, fg="black",
                                   font="serif 12 bold")
        self.btn_register.place(x=100, y=190)

    """Interface to register a user inorder to login"""

    def register_here(self):
        self.frame_image.grid_forget()
        self.frame_right.grid_forget()
        self.interface.title('Registration Page')
        self.interface.config(bg='lightgray')

        self.main_frame = Frame(self.interface, width=700, height=900, bg="white")
        self.main_frame.place(x=155, y=20)

        self.frame1 = Frame(self.main_frame, width=810, height=500, bg="grey")
        self.frame1.place(x=0, y=0)


        # loading images in frame2_right###

        self.bg_1 = Image.open('registerhere.jpg')
        self.resized_1 = self.bg_1.resize((350, 700), Image.ANTIALIAS)
        self.image2_1= ImageTk.PhotoImage(self.resized_1)
        #
        self.bg_image_1 = Label(self.frame1, image=self.image2_1)
        self.bg_image_1.pack(pady=1)


        self.label = Label(self.frame1, text="WE KINDLY REQUEST YOU", font=("calibri", 12,"bold"),
                 fg="red",bg="white")
        self.label.place(x=150, y=250)


        self.label_help = Label(self.frame1, text="TO REGISTER HERE!!!", font=("calibri", 12,"bold"),
                  fg="red",bg="white")
        self.label_help.place(x=160, y=273)
        #
        self.label_fname = Label(self.main_frame, text="First Name ", font=("calibri", 13, "bold"),bg="white")
        self.label_fname.place(x=360, y=10)

        self.entry_fname = Entry(self.main_frame, font=('calibri', 13, 'bold'), bg="lightgrey")
        self.entry_fname.place(x=460, y=10, height=28,width=230)
        #
        self.label_middle_name = Label(self.main_frame, text="Middle Name", font=("calibri", 13, "bold"),bg="white")
        self.label_middle_name.place(x=360, y=50)
        #
        self.entry_middle_name = Entry(self.main_frame, font=('calibri', 13, 'bold'), bg="lightgrey")
        self.entry_middle_name.place(x=475, y=50, height=30, width=200)
        # #
        self.label_lname = Label(self.main_frame, text="Last Name", font=("calibri", 15, "bold"),bg="white")
        self.label_lname.place(x=360, y=90)
        #
        self.entry_lname_name = Entry(self.main_frame, font=('calibri', 15, 'bold'), bg="lightgrey")
        self.entry_lname_name.place(x=460, y=90, height=30, width=230)
        # #
        self.label_age = Label(self.main_frame, text="Age", font=("calibri", 13, "bold"),bg="white")
        self.label_age.place(x=360, y=130)
        #
        self.entry_age_name = Entry(self.main_frame, font=('calibri', 15, 'bold'), fg="black", bg="lightgrey")
        self.entry_age_name.place(x=460, y=130, height=30, width=230)
        #
        self.label_num = Label(self.main_frame, text="Phone No.", font=("calibri", 13, "bold"),bg="white")
        self.label_num.place(x=360, y=175)
        #
        self.entry_num = Entry(self.main_frame, font=('calibri', 15, 'bold'), fg="black", bg="lightgrey")
        self.entry_num.place(x=460, y=170, height=30, width=230)
        #
        self.label_gender = Label(self.main_frame, text="Gender", font=("calibri", 13, "bold"),bg="white")
        self.label_gender.place(x=360, y=213)
        #
        self.entry_gender = ttk.Combobox(self.main_frame, state="readonly", values=["Male", "Female", "Others"],
                                          font=("calibri", 13, "bold"),)
        self.entry_gender.place(x=460, y=210, height=30, width=230)
        self.entry_gender.set("Select")
        self.label_username = Label(self.main_frame, text="Username", font=("calibri", 13, "bold"),bg="white")
        self.label_username.place(x=360, y=250)
        #
        self.entry_username = Entry(self.main_frame, font=('calibri', 15, 'bold'), fg="black", bg="lightgrey")
        self.entry_username.place(x=460, y=250, height=30, width=230)
        #
        self.label_password = Label(self.main_frame, text="Password", font=("calibri", 13, "bold"),bg="white")
        self.label_password.place(x=360, y=290)
        #
        self.entry_password = Entry(self.main_frame, show="*", font=('calibri', 15, 'bold'), fg="black", bg="lightgrey")
        self.entry_password.place(x=460, y=290, height=30, width=230)
        #
        self.label_confirm_password = Label(self.main_frame, text="Confirm Password", font=("calibri", 13, "bold"),bg="white")
        self.label_confirm_password.place(x=360, y=330)

        self.entry_confirm_password = Entry(self.main_frame, show="*", font=('calibri', 15, 'bold'), fg="black",
                                            bg="lightgrey")
        self.entry_confirm_password.place(x=500, y=330, height=30, width=190)
        #
        self.button_register = Button(self.main_frame, text='Register', fg="red",command=self.save,
                                      font="serif 16 bold")
        self.button_register.place(x=460, y=400, height=30, width=95)
        self.button_back = Button(self.main_frame, text="Back", fg="Black",command=lambda: self.back(self.main_frame),
                                  font="serif 16 bold")
        self.button_back.place(x=460, y=480, height=30, width=95)

    def register_photo(self):
        self.cap = cv.VideoCapture(0)
        self.interval = 1
        self.photo_frame = Frame(self.frame1, width=600, height=800, bg="red")
        self.photo_frame.place(x=0, y=0)
        self.canvas = Canvas(self.photo_frame, width=600, height=800)
        self.canvas.place(x=0, y=0)

        self.sav_button = Button(self.photo_frame, text='Save', fg="purple",
                                 font="serif 16 bold",command=self.save_pic)
        self.sav_button.place(x=10, y=430, width=100, height=50)
        self.exit_button = Button(self.photo_frame, text='Exit', fg="purple",
                                  font="serif 16 bold")
        self.exit_button.place(x=150, y=430, width=100, height=50)
        self.update_image()

    def update_image(self):
        self.ret, self.vid = self.cap.read()
        self.face = self.data.detectMultiScale(self.vid, scaleFactor=1.1, minNeighbors=4, minSize=(100, 100))

        try:
            if self.face != ():
                for x, y, h, w in self.face:
                    self.crop_img = self.vid[y:y + h + 30, x:x + w + 30]
                    self.image = cv.cvtColor(self.crop_img, cv.COLOR_BGR2RGB)
            else:
                self.image = cv.cvtColor(self.vid, cv.COLOR_BGR2RGB)

            self.image = cv.resize(self.image, dsize=(450, 350), interpolation=cv.INTER_CUBIC)
            self.image = Image.fromarray(self.image)  # to PIL format
            self.image = ImageTk.PhotoImage(self.image)  # to ImageTk format
            self.canvas.create_image(200, 250, image=self.image)

        except:
            pass
        if self.ret != False:
            self.photo_frame.after(self.interval, self.update_image)

        else:
            pass

    def login_here(self):
        self.frame_image.grid_forget()
        self.frame_right.grid_forget()
        self.interface.title('Login Page')
        self.interface.config(bg="lightblue")

        self.window_frame=Frame(self.interface,width=1080,height=600)
        self.window_frame.place(x=0,y=0)

        self.login_frame = Frame(self.window_frame, width=850, height=500)
        self.login_frame.place(x=120, y=48)


        self.head_frame = Frame(self.window_frame,width=650,height=30,bg="lightblue")
        self.head_frame.place(x=200,y=10)

        self.label_name=Label(self.head_frame,text="CCTV SURVEILLANCE DEPARTMENT EMPLOYEE LOGIN SYSTEM", font=("calibri", 15, "bold"),bg="white")
        self.label_name.place(x=80,y=0)

        # loading images in login_frame####
        self.bg = ImageTk.PhotoImage(file="unknown.jpg")
        self.bg_image = Label(self.login_frame, image=self.bg)
        self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

        self.login_rightframe = Frame(self.login_frame, width=310,height=280,bg="skyblue")
        self.login_rightframe.place(x=490, y=110)


        self.desc = Label(self.login_frame, text="Login to Use the Program", font=("Goudy old sytly", 10, "bold"),
                          bg='skyblue')
        self.desc.place(x=490, y=88)


        self.label_username = Label(self.login_rightframe, text="Username", font="cambria 18 bold",bg='skyblue')
        self.label_username.place(x=0, y=0)

        self.label_username_entry = Entry(self.login_rightframe, width=30, bg="lightgray", font="serif 12")
        self.label_username_entry.place(x=5, y=35, width=300, height=30)

        self.label_password = Label(self.login_rightframe, text="Password", font="cambria 18 bold",bg='skyblue')
        self.label_password.place(x=0, y=69)

        self.label_password_entry = Entry(self.login_rightframe, show="*", width=30, bg="lightgray", font="serif 12  ",
                                          fg="black")
        self.label_password_entry.place(x=5, y=105, width=300, height=30)

        self.login_btn = Button(self.login_rightframe, text="LogIn", width=20, fg="purple",bg='lightgreen', font="serif 14 bold",command=self.login)
        self.login_btn.place(x=30, y=155)

        self.forget_btn = Button(self.login_rightframe, text="Forget Password?", fg='red', font="serif 12 bold")
        self.forget_btn.place(x=75, y=205)

        self.back_btn= Button(self.login_rightframe,text="Back",fg="Blue",font='serif 10 bold',command=lambda: self.back(self.window_frame))
        self.back_btn.place(x=140,y=245)

        self.counter = 0


        """Method to access one step behind interface"""

    def back(self, frame):
        frame.place_forget()
        self.frame_image.grid(row=0, column=0, padx=8, pady=5)
        self.frame_right.grid(row=0, column=1, padx=10, pady=5)
        self.interface.title('''An Intensive Research on application of machine learning techniques to improve the Physical
        Security in Banking Environment using Surveillance System.''')
        # try:
        #     if self.ret != False:
        #         self.cap.release()
        #         cv.destroyAllWindows()
        #
        #     else:
        #         pass
        #
        # except:
        #     pass

    def save_pic(self):
        path = os.getcwd() + "\\photos_data"

        if self.entry_username.get != None:
            self.gray = cv.cvtColor(self.crop_img, cv.COLOR_BGR2GRAY)
            cv.imwrite(os.path.join(path, f"{self.entry_username.get()}" + ".jpg"), self.gray)



        else:
            messagebox.showerror("error", "Enter valid username")

        cv.destroyAllWindows()
        self.cap.release()


       # self.clear()
        self.back(self.main_frame)

        messagebox.showinfo('Successful', 'Registered success')

    def save(self):
        self.con = Connection()
        self.cur = self.con.cur

        try:
            self.fname = self.entry_fname.get().upper()
            self.mname = self.entry_middle_name.get().upper()
            self.lname = self.entry_lname_name.get().upper()
            self.age = self.entry_age_name.get()
            self.phone = self.entry_num.get()
            self.gen = self.entry_gender.get()
            self.username = self.entry_username.get()
            self.password = self.entry_password.get()
            self.conform_pass = self.entry_confirm_password.get()

            if self.fname and self.lname and self.age and self.phone and self.gen and self.username and self.password and self.conform_pass:
                if self.password == self.conform_pass:
                    self.password = pass_to_hash.encrypt_string(self.password)

                    self.value = (
                    self.fname, self.mname, self.lname, self.age, self.phone, self.gen, self.username, self.password)
                    self.query = 'insert into registration_tbl values(%s,%s,%s,%s,%s,%s,%s,%s)'
                    self.cur.execute(self.query, self.value)
                    self.register_photo()


                else:
                    messagebox.showerror("Error", "Password do not match")
            else:
                messagebox.showerror("Error", "Fill all Data")
        except mysql.connector.Error as e:
            messagebox.showerror('Error', e)
        self.con.close()

    """Face login system Using facial recognition system"""

    def face_login(self, username):
        known_image = face_recognition.load_image_file("photos_data/" + f"{username}.jpg")
        cap = cv.VideoCapture(0)
        main_img = cv.imread("photos_data/" + f"{username}.jpg")
        while cap.isOpened():
            cv.imshow("photo", main_img)
            try:
                if cv.waitKey(1) & 0xFF == ord("q"):
                    break
                ret, frame = cap.read()
                frame = cv.flip(frame, 1)

                cv.rectangle(frame, (175, 40), (525, 350), (0, 255, 0), 3)
                if cv.waitKey(1) & 0xFF == 13:
                    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                    cv.imwrite("filename" + ".jpg", frame)
                    known_encoding = face_recognition.face_encodings(known_image)[0]
                    unknown_image = face_recognition.load_image_file("filename.jpg")
                    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
                    results = face_recognition.compare_faces([known_encoding], unknown_encoding, tolerance=0.5)

                    if results[0]:
                        print("Matched")
                        final_result = True
                        break
                    else:
                        frequency = 2500  # Set Frequency To 2500 Hertz
                        duration = 1000  # Set Duration To 1000 ms == 1 second
                        Beep(frequency, duration)

                cv.imshow("Live", frame)
            except IndexError:
                print("No face is Detected ! ! !")
        cap.release()
        cv.destroyAllWindows()
        return final_result

    # **********************************************************************************************************************************

    "Accessing database to login as a appropriate user"

    def login(self):
        self.con = Connection()
        self.cur = self.con.cur

        """ .................File handling for retrieving and comparing data to login..................."""
        self.username1 = self.label_username_entry.get()
        self.password1 = self.label_password_entry.get()
        self.password1 = pass_to_hash.encrypt_string(self.password1)
        try:
            if self.username1 and self.password1:
                self.query = f'select password from registration_tbl where username="{self.username1}"'
                self.cur.execute(self.query)
                self.result = self.cur.fetchone()
                if self.result == None:
                    messagebox.showerror("Error", "Invalid Username/Password ! ! !")
                    self.login_clear()
                else:
                    if self.result[0] == self.password1:
                        if self.face_login(self.username1) == True:
                            messagebox.showinfo("login", "Successfully logged in")
                            self.load_backend()
                            self.login_clear()
                            self.counter = 0
                    else:
                        self.counter += 1
                        if self.counter >= 3:
                            messaging.send_error_login()
                            self.err_sound()
                        print(self.counter)
                        messagebox.showerror("Error", "Username or password do not matched")
                        self.login_clear()
            else:
                messagebox.showerror("Error", "Username or password is empty")


        except mysql.connector.Error as e:
            messagebox.showerror("Error", e)

        self.con.close()


    def load_backend(self):
        self.login_frame.grid_forget()
        self.head_frame.grid_forget()
        self.interface.title('Internal')

        self.detection_int = Frame(self.interface, width=1080, height=600, bg="black")
        self.detection_int.place(x=0, y=0)

        self.frame_l = Frame(self.detection_int, width=240, height=580, bg="skyblue")
        self.frame_l.place(x=10, y=10)

        self.frame_r = Frame(self.detection_int, width=810, height=450, bg="skyblue")
        self.frame_r.place(x=260, y=10)

        self.frame_dl = Frame(self.detection_int, width=810, height=120, bg="skyblue")
        self.frame_dl.place(x=260, y=470)

        self.weapon_frame=Frame(self.frame_l,width=220,height=180,bg="red")
        self.weapon_frame.place(x=10,y=10)

        self.smoke_fire_frame=Frame(self.frame_l,width=220,height=180,bg="red")
        self.smoke_fire_frame.place(x=10,y=250)

        #########image for weapon#############
        self.weapon_1 = Image.open('weapon.jpg')
        self.resize_weapon  = self.weapon_1.resize((220, 180), Image.ANTIALIAS)
        self.image_weapon = ImageTk.PhotoImage(self.resize_weapon)
        #
        self.bg_weapon_1 = Label(self.weapon_frame, image=self.image_weapon)
        self.bg_weapon_1.pack(pady=1)

        #########image for smoke_fire#########
        self.fire_1 = Image.open('fire.jpg')
        self.resize_fire = self.fire_1.resize((220, 180), Image.ANTIALIAS)
        self.image_fire = ImageTk.PhotoImage(self.resize_fire)
        #
        self.bg_fire_1 = Label(self.smoke_fire_frame, image=self.image_fire)
        self.bg_fire_1.pack(pady=1)

        Button(self.frame_l, text="Weapon Detection", font=("cambria", 13, "bold"), fg="black", height=1,command=lambda: weapon_detect.weapon(self.frame_r,self.frame_dl),
               width=15).place(x=45, y=196)
        Button(self.frame_l, text="Fire_Smoke Detection", font=("cambria", 13, "bold"), fg="black", height=1,command=lambda: smoke_fire.smoke(self.frame_r,self.frame_dl),
               width=18).place(x=29, y=436)
        # Button(self.frame_l, text="Overall interface", font=("cambria", 15, "bold"), fg="green", height=2, width=18,
        #        command=lambda: self.cam_access()).place(x=5, y=405)
        Button(self.frame_l, text="Exit", font=("cambria", 10, "bold"), fg="green", height=1, width=12).place(x=6, y=500)

        Label(self.frame_dl, text="Information Panel",font=("Courier", 20), bg = "black", fg="white").place(x=185, y=0)

    """Accesing cam after login to detect things"""

    def login_clear(self):
        self.label_username_entry.delete(0, END)
        self.label_password_entry.delete(0, END)

    """Save the users data in the database for future access"""
    """Save the users data in the database for future access"""

    def err_sound(self):
        def do(time=200):
            Beep(261 * 2, time)

        def do_sharp(time=200):
            Beep(277 * 2, time)

        def rae(time=200):
            Beep(293 * 2, time)

        def rae_sharp(time=200):
            Beep(311 * 2, time)

        def me(time=200):
            Beep(329 * 2, time)

        def fa(time=time):
            Beep(349 * 2, time)

        def fa_sharp(time=200):
            Beep(369 * 2, time)

        def sol(time=200):
            Beep(392 * 2, time)

        def sol_sharp(time=200):
            Beep(415 * 2, time)

        def ra(time=200):
            Beep(440 * 2, time)

        def ra_shar(time=200):
            Beep(446 * 2, time)

        def si(time=200):
            Beep(493 * 2, time)

        def high_do(time=200):
            Beep(523 * 2, time)

        def high_do_sharp(time=200):
            Beep(554 * 2, time)

        def high_rae(time=200):
            Beep(587 * 2, time)

        def high_rae_sharp(time=200):
            Beep(622 * 2, time)

        def high_me(time=200):
            Beep(659 * 2, time)

        def high_fa(time=200):
            Beep(698 * 2, time)

        def high_fa_sharp(time=200):
            Beep(739 * 2, time)

        def high_sol(time=200):
            Beep(783 * 2, time)

        def high_sol_sharp(time=200):
            Beep(830 * 2, time)

        def high_ra(time=200):
            Beep(880 * 2, time)

        def high_ra_sharp(time=200):
            Beep(932 * 2, time)

        def high_si(time=200):
            Beep(987 * 2, time)

        def main_melody():
            fa_sharp()
            time.sleep(0.2)
            fa_sharp()
            high_do_sharp()
            si()
            time.sleep(0.2)
            ra()
            time.sleep(0.2)
            sol_sharp()
            time.sleep(0.2)
            sol_sharp()
            sol_sharp()
            si()
            time.sleep(0.2)
            ra()
            sol_sharp()
            fa_sharp()
            time.sleep(0.2)
            fa_sharp()
            high_ra()
            high_sol_sharp()
            high_ra()
            high_sol_sharp()
            high_ra()

            fa_sharp()
            time.sleep(0.2)
            fa_sharp()
            high_ra()
            high_sol_sharp()
            high_ra()
            high_sol_sharp()
            high_ra()

        def sub_melody():
            for i in range(4):
                ra(200)

            for i in range(4):
                high_do_sharp(200)

            for i in range(4):
                si(200)
            for i in range(4):
                high_me(200)

            for i in range(12):
                high_fa_sharp(200)

            si(200)
            ra(200)
            sol_sharp(200)
            me(200)

        main_melody()
        sub_melody()


interface = Tk()
gui = Thesis_Project(interface)
interface.mainloop()