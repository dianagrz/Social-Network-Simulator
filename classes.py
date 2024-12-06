from data_structures.myqueue import Queue
from data_structures.heap_queue import Heap
from data_structures.hash_set import HashSet
from data_structures.hash_map import HashMap
from data_structures.linked_lists import LinkedList

import string, random

class SocialNet:
    def __init__(self):
        self.users = HashMap()
        self.logged_user = None
        self.posts = HashMap()
        self.postPreference = Heap()
        
        self.users_database = "databases/users_database.txt"
        self.posts_database = "databases/posts_database.txt"
        self.comments_database = "databases/comments_database.txt"
        self.likes_database = "databases/likes_database.txt"
        self.followers_database = "databases/followers_database.txt"
        
    def load_data(self):
        #I am using .strip() to avoid line breaks in the data
        with open(self.users_database, 'r') as file:
            for line in file:
                username, name, password = line.split('|')
                new_user = User(username, name, password.strip())
                self.users.put(username, new_user)
     
        with open(self.posts_database, 'r') as file:
            for line in file:
                post_id, username, content = line.split('|')
                user = self.users.get(username)
                new_post = user.post(post_id, content.strip())
                #new_post = Post(post_id, content.strip(), user)
                self.posts.put(post_id, new_post)
                
        with open(self.comments_database, "r") as file:
            for line in file:
                post_id, username, content = line.split('|')
                user = self.users.get(username)
                self.posts.get(post_id).comment(user, content.strip())
                
        with open(self.likes_database, "r") as file:
            for line in file:
                post_id, username = line.split('|')
                user = self.users.get(username.strip())
                if not user:
                    print(f"{username} not found")
                self.posts.get(post_id).like(user)
        
        with open(self.followers_database, "r") as file:
            for line in file:
                username1, username2 = line.split('|')
                user1 = self.users.get(username1)
                user2 = self.users.get(username2.strip())
                user1.follow(user2)
    
    def login_user(self, username, password):
        user = self.users.get(username)
        if not user:
            print("This user doesn't exist")
            return
            #raise Exception("This user doesn't exist")
        elif user.password != password:
                raise Exception("Wrong password")
                return
        else:
            self.logged_user = user
            print("logged in")
            
        for _ , post in self.posts:
            priority = 0
            if post.user in self.logged_user.following:
                priority += 2
            if post.user in self.logged_user.followers:
                priority += 1
            self.postPreference.enqueue(priority, post)
                
    def new_user(self, username, name, password):
        if self.users.get(username):
            raise Exception("This username already exists")
        user = User(username, name, password)
        self.users.put(username, user)
        
        with open(self.users_database, "a") as file:
            file.write(f"{username}|{name}|{password}\n")
            
        return user

    def make_post(self, content):
        post_id = ""
        char = string.ascii_lowercase +string.digits
        for i in range(random.randint(10, 15)):
            post_id += random.choice(char)
            
        while post_id in self.posts:
            post_id = ""
            for i in range(random.randint(10, 15)):
                post_id += random.choice(char)
        
        new_post = self.logged_user.post(post_id, content)
        
        with open(self.posts_database, "a") as file:
            file.write(f"{post_id}|{self.logged_user.username}|{content}\n")
            
        return new_post
    
    def like_post(self, post_id):
        if not self.logged_user:
            raise Exception("Need to log in for this action")
            
        post = self.posts.get(post_id)
        post.like(self.logged_user)
        
        with open(self.likes_database, "a") as file:
            file.write(f"{post_id}|{self.logged_user.username}\n")
    
    def delete_like(self, post):
        post.delete_like(self.logged_user)
        
        target_line = f"{post.post_id}|{self.logged_user.username}"
        with open(self.likes_database, "r") as file:
            lines = file.readlines()
        with open(self.likes_database, "w") as file:
            for line in lines:
                if not self.match(line, target_line):
                    file.write(line)
        
    def comment_post(self, post_id, content):
        if not self.logged_user:
            raise Exception("Need to log in for this action")
            
        post = self.posts.get(post_id)
        post.comment(self.logged_user, content)
        
        with open(self.comments_database, "a") as file:
            file.write(f"{post_id}|{self.logged_user.username}|{content}\n")
        
    def follow_user(self, user):
        self.logged_user.follow(user)
        
        with open(self.followers_database, "a") as file:
            file.write(f"{self.logged_user.username}|{user.username}\n")
    
    def unfollow_user(self, user):
        self.logged_user.unfollow(user)
        
        username1 = self.logged_user.username
        username2 = user.username
        
        target_line = f"{username1}|{username2}"
        with open(self.followers_database, "r") as file:
            lines = file.readlines()
        
        with open(self.followers_database, "w") as file:
            for line in lines:
                if not self.match(line, target_line):
                    file.write(line)
    
    def match(self, line, text):
        line = line.strip()
        text = text.strip()
        for i in range(len(text)):
            if line[i] != text[i]:
                return False
        return True
    
    def search(self, keyword):
        with open(self.users_database, "r") as file:
            lines = file.readlines()
        
        matches = []
        for line in lines:
            if self.kmp(line.strip(), keyword) is not None:
                username, name, password = line.split('|')
                matches.append(username)
        return matches
    
    def kmp(self, text, pattern):
        def pi_table(pattern):
            m = len(pattern)
            pi = [-1]*m
            k = -1
            
            for i in range(1, m):
                while k > -1 and pattern[i] != pattern[k+1]:
                    k = pi[k] 
                if pattern[i] == pattern[k+1]:
                    k += 1
                pi[i] = k 
            return pi
        
        n = len(text)
        m = len(pattern)
        pi = pi_table(pattern)
        
        k = -1
        for i in range(n):
            while k > -1 and text[i] != pattern[k+1]:
                k = pi[k]
                
            if text[i] == pattern[k+1]:
                k += 1
            if k+1 >= m:
                return i - m + 1
    
class User:
    def __init__(self, username, name, password):
        self.username = username
        self.name = name
        self.password = password
        
        self.posts = LinkedList()
        self.following = HashSet()
        self.followers = HashSet()
        self.notifications = Queue()
    
    def follow(self, user):
        self.following.add(user)
        user.followers.add(self)
        user.notifications.enqueue(f"{self.name} now follows you.")
        
    def unfollow(self, user):
        if user not in self.following:
            raise Exception("Not in following list")
        else:
            self.following.remove(user)
            user.followers.remove(self)
    
    def post(self, post_id, content):
        new_post = Post(post_id, content, self)
        self.posts.append(new_post)
        return new_post
    
    def is_followed_by(self, user):
        return user in self.followers
    
class Post:
    def __init__(self, post_id, content, user):
        self.post_id = post_id
        self.user = user
        self.content = content
        
        self.likes = HashSet()
        self.comments = Queue()
    
    def like(self, user):
        self.likes.add(user)
        self.user.notifications.enqueue(f"{user.name} liked your post.")
        
    def delete_like(self, user):
        self.likes.remove(user)
    
    def comment(self, user, content):
        self.comments.enqueue((user, content))
        self.user.notifications.enqueue(f"{user.name} commented on one of your posts")
        
    def is_liked_by(self, user):
        return user in self.likes