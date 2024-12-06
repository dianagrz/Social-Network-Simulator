import tkinter as tk
from tkinter import ttk
from classes import SocialNet, User, Post

class App:
    def __init__(self):
        self.net = SocialNet()
        self.net.load_data()
        
        self.USER = None
        
        self.screen = tk.Tk()
        self.screen.geometry("350x350")
        self.screen.title("LOG IN TO SIM NET")
        
        self.login_screen()

        self.screen.mainloop()
    
    def login_screen(self):
        
        def log_in():
            username = username_tf.get()
            password = password_tf.get()
            self.net.login_user(username, password)
            self.USER = self.net.logged_user
            for widget in self.screen.winfo_children():
                widget.destroy()
            self.main_feed_screen()

        def sign_up():
            for widget in self.screen.winfo_children():
                widget.destroy()
            self.signup_screen()

        title_lab = tk.Label(self.screen, text = "Sim Net", font=('Cooper Black', 16), )
        username_lab = tk.Label(self.screen, text = "Username: ")
        password_lab = tk.Label(self.screen, text = "Password: ")
        signup_lab = tk.Label(self.screen, text = "Don't have an account?")

        username_tf = tk.Entry(self.screen)
        password_tf = tk.Entry(self.screen)

        login_btn = tk.Button(self.screen, text = "Login", command=log_in)
        signup_btn = tk.Button(self.screen, text = "Sign Up", command=sign_up)

        title_lab.pack()
        username_lab.pack()
        username_tf.pack()
        password_lab.pack()
        password_tf.pack()
        login_btn.pack()
        signup_lab.pack()
        signup_btn.pack()

        self.screen.mainloop()

    
    def signup_screen(self):
        def sign_up():
            first_name = first_name_tf.get()
            last_name = last_name_tf.get()
            username = username_tf.get()
            password = password_tf.get()
            name = first_name.strip() + " " + last_name.strip()
            self.net.new_user(username, name, password)
            self.USER = self.net.logged_user
            for widget in self.screen.winfo_children():
                widget.destroy()
            self.login_screen()

        title_lab = tk.Label(self.screen, text = "Sim Net", font=('Cooper Black', 16), )
        first_name_lab = tk.Label(self.screen, text = "First name: ")
        last_name_lab = tk.Label(self.screen, text = "Last name: ")
        username_lab = tk.Label(self.screen, text = "Username: ")
        password_lab = tk.Label(self.screen, text = "Password: ")
        disclaimer_lab = tk.Label(self.screen, text = "You will have to log in afterwards")

        username_tf = tk.Entry(self.screen)
        password_tf = tk.Entry(self.screen)
        first_name_tf = tk.Entry(self.screen)
        last_name_tf = tk.Entry(self.screen)

        signup_btn = tk.Button(self.screen, text = "Sign Up", command=sign_up)

        title_lab.pack()
        first_name_lab.pack()
        first_name_tf.pack()
        last_name_lab.pack()
        last_name_tf.pack()
        username_lab.pack()
        username_tf.pack()
        password_lab.pack()
        password_tf.pack()
        signup_btn.pack()
        disclaimer_lab.pack()

        self.screen.mainloop()
    
    def main_feed_screen(self):
        self.screen.geometry("1200x600")
        self.screen.title("SIM NET")

        tabControl = ttk.Notebook(self.screen) 
          
        tab1 = ttk.Frame(tabControl) 
        tab2 = ttk.Frame(tabControl) 
        tab3 = ttk.Frame(tabControl) 
        tab4 = ttk.Frame(tabControl) 
          
        tabControl.add(tab1, text ='Main') 
        tabControl.add(tab2, text ='My Profile') 
        tabControl.add(tab3, text ='Notifications') 
        tabControl.add(tab4, text ='Search') 
        tabControl.pack(expand = 1, fill ="both") 
        
        self.all_posts_tab(tab1)
        self.my_profile_tab(tab2)
        self.notifications_tab(tab3)
        self.search_tab(tab4)
    
    def all_posts_tab(self, tab):
        canvas = tk.Canvas(tab)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        content_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=content_frame, anchor="nw")

        while self.net.postPreference.get_root():
            square_frame = tk.Frame(content_frame, relief=tk.RAISED, borderwidth=2)
            _, curr_post = self.net.postPreference.dequeue()
            user = curr_post.user.username
            text = curr_post.content
            display_text = f"{user}: {text}"
            text_var = tk.StringVar()
            text_var.set(display_text)
            label = tk.Label(square_frame, 
                             textvariable=text_var, 
                             font = ("Arial", 16),                   
                             pady=5,
                             padx=5,
                             justify=tk.LEFT,
                             wraplength=1000,
                             )
            button = tk.Button(square_frame, text="See post", command=lambda curr_post=curr_post: self.see_post(curr_post))
            label.grid(row=0, column =0, columnspan=4, sticky="w")
            button.grid(row=0, column=4, padx=10, sticky="e")
            
            square_frame.grid_columnconfigure(0, weight=1)  
            square_frame.grid_columnconfigure(4, weight=0)  
            
            square_frame.pack(side="top", pady=15, padx=10, fill="x", expand=True)
            
            def configure_canvas(event):
                canvas.configure(scrollregion=canvas.bbox("all"))

            content_frame.bind("<Configure>", configure_canvas)
    
    def my_profile_tab(self, tab):
        name_var = tk.StringVar()
        name_var.set(self.USER.name)
        username = f"@{self.USER.username}"
        username_var = tk.StringVar()
        username_var.set(username)
        followers = f"Followers: {len(self.USER.followers)}"
        followers_var = tk.StringVar()
        followers_var.set(followers)
        following = f"Following: {len(self.USER.following)}"
        following_var = tk.StringVar()
        following_var.set(following)
        labelName = tk.Label(tab, textvariable=name_var, font=('Arial', 16, 'bold'))
        labelUsername = tk.Label(tab, textvariable=username_var)
        labelFollowers = tk.Label(tab, textvariable=followers_var)
        labelFollowing = tk.Label(tab, textvariable=following_var)

        tfPost = tk.Entry(tab)

        btnFollowing = tk.Button()
        btnFollowers = tk.Button()
        
        my_profile_canvas = tk.Canvas(tab)
        my_profile_scrollbar = ttk.Scrollbar(my_profile_canvas, orient="vertical", command=my_profile_canvas.yview)
        my_profile_canvas.configure(yscrollcommand=my_profile_scrollbar.set)
        my_profile_canvas.grid(row=2, column=1, rowspan=3, columnspan=2, sticky="nswe")
        my_profile_scrollbar.pack(side="right", fill="y")
        my_profile_content_frame = ttk.Frame(my_profile_canvas)
        my_profile_canvas.create_window((0, 0), window=my_profile_content_frame, anchor="nw")
        
        def post():
            content = tfPost.get()
            tfPost.delete(0, "end")
            post = self.net.make_post(content)
            square_frame = tk.Frame(my_profile_content_frame, relief=tk.RAISED, borderwidth=2)
            text_var = tk.StringVar()
            text_var.set(content)
            label = tk.Label(square_frame, 
                             textvariable=text_var, 
                             font = ("Arial", 16),                   
                             pady=5,
                             padx=5,
                             justify=tk.LEFT,
                             wraplength=600,
                             )
            button = tk.Button(square_frame, text="See post", command=lambda post=post:self.see_post(post))
            label.grid(row=0, column =0, columnspan=4, sticky="w")
            button.grid(row=0, column=4, padx=10, sticky="e")
            
            square_frame.grid_columnconfigure(0, weight=1)  
            square_frame.grid_columnconfigure(4, weight=0)  
            
            square_frame.pack(pady=10, fill="x", expand=True)
        
        btnFollowers = tk.Button(tab, text="See Followers", command=lambda:self.see_followers(self.USER))
        btnFollowing = tk.Button(tab, text="See Following", command=lambda:self.see_following(self.USER))
        btnPost = tk.Button(tab, text="Post", command=post)
        
        labelName.grid(row=0, column=0)
        labelUsername.grid(row=1, column=0)
        labelFollowing.grid(row=0, column=1)
        labelFollowers.grid(row=1, column=1)
        btnFollowers.grid(row=0, column=2)
        btnFollowing.grid(row=1, column=2)
        tfPost.grid(row=3, column=0, sticky="nsew", padx=10)
        btnPost.grid(row=4, column=0)

        tab.grid_rowconfigure(2, weight=1)
        tab.grid_rowconfigure(3, weight=1)
        tab.grid_rowconfigure(4, weight=1) 
        tab.grid_columnconfigure(0, weight=1) 
        tab.grid_columnconfigure(1, weight=1) 
        tab.grid_columnconfigure(2, weight=1)

        current = self.USER.posts.head
        while current:
            square_frame = tk.Frame(my_profile_content_frame, relief=tk.RAISED, borderwidth=2)
            post = current.data
            text_var = tk.StringVar()
            text_var.set(post.content)
            label = tk.Label(square_frame, 
                             textvariable=text_var, 
                             font = ("Arial", 16),                   
                             pady=5,
                             padx=5,
                             justify=tk.LEFT,
                             wraplength=600,
                             )
            button = tk.Button(square_frame, text="See post", command=lambda post=post:self.see_post(post))
            label.grid(row=0, column =0, columnspan=4, sticky="w")
            button.grid(row=0, column=4, padx=10, sticky="e")
            
            square_frame.grid_columnconfigure(0, weight=1)  
            square_frame.grid_columnconfigure(4, weight=0)  
            
            square_frame.pack(side="top", pady=10, fill="x", expand=True)
            current = current.next 
            
        def configure_canvas(event):
            my_profile_canvas.configure(scrollregion=my_profile_canvas.bbox("all"))

        my_profile_content_frame.bind("<Configure>", configure_canvas)
    
    def notifications_tab(self, tab):
        canvas = tk.Canvas(tab)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        content_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=content_frame, anchor="nw")

        while self.USER.notifications.peek():
            notification = self.USER.notifications.dequeue()
            text_var = tk.StringVar()
            text_var.set(notification)
            label = tk.Label(content_frame, 
                             textvariable=text_var, 
                             font = ("Arial", 16),                   
                             pady=5,
                             padx=5,
                             relief=tk.RAISED,     
                             )
            label.pack(side="top", pady=5, fill="x", expand=True, anchor="center")
             

        def configure_canvas(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        content_frame.bind("<Configure>", configure_canvas)
    
    def search_tab(self, tab):
        labSearch = tk.Label(tab, text="Enter a name or username: ")
        tfKeyword = tk.Entry(tab)
        
        canvas = tk.Canvas(tab)
        scrollbar = ttk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.grid(row=2, column=0, columnspan=3, sticky="nsew")
        scrollbar.pack(side="right", fill="y")
        content_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        
        def search(): 
            keyword = tfKeyword.get()
            matches = self.net.search(keyword)
            
            for widget in content_frame.winfo_children():
                widget.destroy()
            tfKeyword.delete(0, "end")
        
            for option in matches:
                print(option)
                square_frame = tk.Frame(content_frame, relief=tk.RAISED, borderwidth=2)
                user = self.net.users.get(option)
                label = tk.Label(square_frame, 
                                 text=option, 
                                 font = ("Arial", 16),                   
                                 pady=5,
                                 padx=5,
                                 justify=tk.LEFT,
                                 wraplength=600,
                                 )
                button = tk.Button(square_frame, text="See profile", command=lambda user=user:self.see_profile(user))
                label.grid(row=0, column =0, columnspan=4, sticky="w")
                button.grid(row=0, column=4, padx=10, sticky="e")
                
                square_frame.grid_columnconfigure(0, weight=1)  
                square_frame.grid_columnconfigure(4, weight=0)  
                
                square_frame.pack(side="top", pady=10, fill="x", expand=True)
        
        btnSearch = tk.Button(tab, text="Search", command=search)

        labSearch.grid(row=0, column=0, sticky="w")
        tfKeyword.grid(row=1, column=0, sticky="ew")
        btnSearch.grid(row=1, column=1, sticky="w", padx=10)

        tab.grid_columnconfigure(0, weight=2)
        tab.grid_columnconfigure(1, weight=1)
        tab.grid_rowconfigure(2, weight=1)
        
        def configure_canvas(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        content_frame.bind("<Configure>", configure_canvas)
    
    def see_profile(self, user):
        tab = tk.Toplevel(self.screen)
        tab.geometry("1200x600")
        tab.title(f"{user.name}'s profile")
        name_var = tk.StringVar()
        name_var.set(user.name)
        username = f"@{user.username}"
        username_var = tk.StringVar()
        username_var.set(username)
        followers = f"Followers: {len(user.followers)}"
        followers_var = tk.StringVar()
        followers_var.set(followers)
        following = f"Following: {len(user.following)}"
        following_var = tk.StringVar()
        following_var.set(following)
        labelName = tk.Label(tab, textvariable=name_var, font=('Arial', 16, 'bold'))
        labelUsername = tk.Label(tab, textvariable=username_var)
        labelFollowers = tk.Label(tab, textvariable=followers_var)
        labelFollowing = tk.Label(tab, textvariable=following_var)

        tfPost = tk.Entry(tab)

        btnFollowing = tk.Button()
        btnFollowers = tk.Button()
        
        canvas = tk.Canvas(tab)
        scrollbar = ttk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.grid(row=3, column=0, rowspan=3, columnspan=3, sticky="nswe")
        scrollbar.pack(side="right", fill="y")
        content_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        
        
        btnFollowers = tk.Button(tab, text="See Followers", command=lambda:self.see_followers(user))
        btnFollowing = tk.Button(tab, text="See Following", command=lambda:self.see_following(user))
        
        followed_value = user.is_followed_by(self.USER)
        followed = tk.BooleanVar(value=followed_value)

        def follow():
            if followed.get():
                self.net.follow_user(user)
            else:
                self.net.unfollow_user(user)

        btnFollow = ttk.Checkbutton(
            tab,
            text="Follow",
            variable=followed,
            command=follow,
            #style="Toggle.TButton",  # Optional: Custom style
            #selectcolor="VioletRed1"
        )
        
        labelName.grid(row=0, column=0)
        labelUsername.grid(row=1, column=0)
        labelFollowing.grid(row=0, column=1)
        labelFollowers.grid(row=1, column=1)
        btnFollowers.grid(row=0, column=2)
        btnFollowing.grid(row=1, column=2)
        btnFollow.grid(row=2, column=1, sticky="nsew")

        tab.grid_rowconfigure(3, weight=1)
        tab.grid_columnconfigure(0, weight=1) 
        tab.grid_columnconfigure(1, weight=1) 
        tab.grid_columnconfigure(2, weight=1)

        current = user.posts.head
        while current:
            square_frame = tk.Frame(content_frame, relief=tk.RAISED, borderwidth=2)
            post = current.data
            text_var = tk.StringVar()
            text_var.set(post.content)
            label = tk.Label(square_frame, 
                             textvariable=text_var, 
                             font = ("Arial", 16),                   
                             pady=5,
                             padx=5,
                             justify=tk.LEFT,
                             wraplength=1100,
                             )
            button = tk.Button(square_frame, text="See post", command=lambda post=post:self.see_post(post))
            label.grid(row=0, column =0, columnspan=4, sticky="w")
            button.grid(row=0, column=4, padx=10, sticky="e")
            
            square_frame.grid_columnconfigure(0, weight=1)  
            square_frame.grid_columnconfigure(4, weight=0)  
            
            square_frame.pack(side="top", pady=10, fill="x", expand=True)
            current = current.next 
            
        def configure_canvas(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        content_frame.bind("<Configure>", configure_canvas)
    
    def see_post(self, post):
        post_window = tk.Toplevel(self.screen)
        post_window.geometry("1200x600")
        post_window.title(f"{post.user.username}'s post")
        
        labelUsername = tk.Label(post_window, text=post.user.username, font=('Arial', 16, 'bold'))
        btnSeeProfile = tk.Button(post_window, text="See profile", command=lambda user=post.user: self.see_profile(user))

        text_var = tk.StringVar()
        text_var.set(post.content)
        labelContent = tk.Label(post_window, 
                         textvariable=text_var, 
                         font = ("Arial", 16),                   
                         pady=5,
                         padx=5,
                         justify=tk.LEFT,
                         wraplength=600,
                         relief=tk.RAISED,
                        )

        labelLikes = tk.Label(post_window, text="Liked by:")
        labelComments = tk.Label(post_window, text="Comments:")

        canvasLikes = tk.Canvas(post_window)
        scrollbarLikes = ttk.Scrollbar(canvasLikes, orient="vertical", command=canvasLikes.yview)
        canvasLikes.configure(yscrollcommand=scrollbarLikes.set)
        scrollbarLikes.pack(side="right", fill="y")
        contentFrameLikes = ttk.Frame(canvasLikes)
        canvasLikes.create_window((0, 0), window=contentFrameLikes, anchor="nw")
        
        for user in post.likes:
            if user != self.USER:
                square_frame = tk.Frame(contentFrameLikes, relief=tk.RAISED, borderwidth=2)
                label = tk.Label(square_frame, 
                                 text=user.username, 
                                 font = ("Arial", 16),                   
                                 pady=5,
                                 padx=5,
                                 justify=tk.LEFT,
                                 wraplength=400,
                                 )
                button = tk.Button(square_frame, text="See profile", command=lambda user=user: self.see_profile(user))
                label.grid(row=0, column =0, columnspan=4, sticky="w")
                button.grid(row=0, column=4, padx=10, sticky="e")
                
                square_frame.grid_columnconfigure(0, weight=1)  
                square_frame.grid_columnconfigure(4, weight=0)  
                
                square_frame.pack(side="top", pady=15, padx=10, fill="x", expand=True)
            
        canvasComments = tk.Canvas(post_window)
        scrollbarComments = ttk.Scrollbar(canvasComments, orient="vertical", command=canvasComments.yview)
        canvasComments.configure(yscrollcommand=scrollbarComments.set)
        scrollbarComments.pack(side="right", fill="y")
        contentFrameComments = ttk.Frame(canvasComments)
        canvasComments.create_window((0, 0), window=contentFrameComments, anchor="nw")
        
        for comment in post.comments:
            user, content = comment
            text_var = f"{user.username}: {content}"
            label = tk.Label(contentFrameComments, 
                             text=text_var, 
                             font = ("Arial", 16),                   
                             pady=5,
                             padx=5,
                             justify=tk.LEFT,
                             wraplength=800,
                             )
            label.pack(pady=15, padx=10, fill="x", expand=True)
        
        liked_value = post.is_liked_by(self.USER)
        liked = tk.BooleanVar(value=liked_value)

        def like():
            if liked.get():
                self.net.like_post(post.post_id)
            else:
                self.net.delete_like(post)

        btnLike = ttk.Checkbutton(
            post_window,
            text="Like",
            variable=liked,
            command=like,
        )
        
        tfComment = tk.Entry(post_window)
        
        def post_comment():
            content = tfComment.get()
            tfComment.delete(0, "end")
            self.net.comment_post(post.post_id, content)
            text = f"{self.USER.username}: {content}"
            label = tk.Label(contentFrameComments, 
                             text=text, 
                             font = ("Arial", 16),                   
                             pady=5,
                             padx=5,
                             justify=tk.LEFT,
                             wraplength=1000,
                             )

            label.pack(side="top", pady=15, padx=10, fill="x", expand=True, sticky="ew")
            
        
        btnPost = tk.Button(post_window, text="Comment", command=post_comment)

        labelUsername.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        btnSeeProfile.grid(row=0, column=1, sticky="w", pady=5)
        labelContent.grid(row=1, column=0, columnspan=3, padx=10, sticky="nsew")
        labelLikes.grid(row=2, column=0)
        labelComments.grid(row=2, column=1)
        canvasLikes.grid(row=3, column=0, sticky="nsew")
        canvasComments.grid(row=3, column=1, columnspan=2, sticky="nsew")
        btnLike.grid(row=4, column=0)
        tfComment.grid(row=4, column=1, sticky="nswe", pady=10)
        btnPost.grid(row=4, column=2)

        post_window.grid_rowconfigure(3, weight=3)
        post_window.grid_rowconfigure(4, weight=1)
        post_window.grid_columnconfigure(0, weight=1)
        post_window.grid_columnconfigure(1, weight=1)
        post_window.grid_columnconfigure(2, weight=1)
        
        def configure_canvas_comments(event):
            canvasComments.configure(scrollregion=canvasComments.bbox("all"))

        contentFrameComments.bind("<Configure>", configure_canvas_comments)
        
        def configure_canvas_likes(event):
            canvasLikes.configure(scrollregion=canvasLikes.bbox("all"))

        contentFrameLikes.bind("<Configure>", configure_canvas_likes)
        
        post_window.update()
        post_window.mainloop()
        
    
    def see_followers(self, user):
        window = tk.Toplevel(self.screen)
        window.geometry("600x600")
        window.title(f"{user.username}'s followers")
        
        canvas = tk.Canvas(window)
        scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        content_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=content_frame, anchor="nw")

        for follower in user.followers:
            square_frame = tk.Frame(content_frame, relief=tk.RAISED, borderwidth=2)
            label = tk.Label(square_frame, 
                             text=follower.username, 
                             font = ("Arial", 16),                   
                             pady=5,
                             padx=5,
                             justify=tk.LEFT,
                             wraplength=1000,
                             )
            button = tk.Button(square_frame, text="See profile", command=lambda follower=follower: self.see_profile(follower))
            label.grid(row=0, column =0, columnspan=4, sticky="w")
            button.grid(row=0, column=4, padx=10, sticky="e")
            
            square_frame.grid_columnconfigure(0, weight=1)  
            square_frame.grid_columnconfigure(4, weight=0)  
            
            square_frame.pack(side="top", pady=15, padx=10, fill="x", expand=True)
             

        def configure_canvas(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        content_frame.bind("<Configure>", configure_canvas)
    
    def see_following(self, user):
        window = tk.Toplevel(self.screen)
        window.geometry("600x600")
        window.title(f"{user.username}'s followed")
        
        canvas = tk.Canvas(window)
        scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        content_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=content_frame, anchor="nw")

        for following in user.followers:
            square_frame = tk.Frame(content_frame, relief=tk.RAISED, borderwidth=2)
            label = tk.Label(square_frame, 
                             text=following.username, 
                             font = ("Arial", 16),                   
                             pady=5,
                             padx=5,
                             justify=tk.LEFT,
                             wraplength=1000,
                             )
            button = tk.Button(square_frame, text="See profile", command=lambda following=following: self.see_profile(following))
            label.grid(row=0, column =0, columnspan=4, sticky="w")
            button.grid(row=0, column=4, padx=10, sticky="e")
            
            square_frame.grid_columnconfigure(0, weight=1)  
            square_frame.grid_columnconfigure(4, weight=0)  
            
            square_frame.pack(side="top", pady=15, padx=10, fill="x", expand=True)
             

        def configure_canvas(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        content_frame.bind("<Configure>", configure_canvas)
    
if __name__=="__main__":
    app = App()