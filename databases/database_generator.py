import random
import string
from data_structures.hash_set import HashSet

names = ["Emma", "Liam", "Olivia", "Noah", "Sophia", "Elijah", "Isabella", "James", "Mia", "Benjamin",
"Charlotte", "Lucas", "Amelia", "Mason", "Ava", "Ethan", "Harper", "Alexander", "Evelyn", "Henry",
"Abigail", "Jackson", "Ella", "Sebastian", "Scarlett", "Aiden", "Grace", "Matthew", "Chloe", "Samuel",
"Victoria", "David", "Aria", "Joseph", "Luna", "Carter", "Layla", "Owen", "Zoey", "Wyatt",
"Lily", "Dylan", "Ellie", "Luke", "Hannah", "Gabriel", "Aurora", "Caleb", "Penelope", "Levi"]

last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
"Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
"Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
"Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
"Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts"]

comments = ["Wow, this is so insightful!", "Thanks for sharing, this made my day!", "Is there a source for this?", "This is so relatable!", "I never thought about it this way!", "Can’t agree more with this!", "Haha, this is gold!", "What inspired this post?", "Totally bookmarking this!", 
            "This is exactly what I needed today!", "Mind blown!", "Such a wholesome moment.", "Couldn’t agree more.", "Quick question about this!", "This resonates deeply with me.", "Brilliantly said!", "I love this perspective.", "This brought a smile to my face!", "Do you have more on this?", 
            "Such a powerful message.", "Love this reminder.", "This post is so underrated.", "Wow, I didn’t know that!", "Thanks for the positivity!", "Any tips for implementing this?", "This is worth sharing widely.", "This is a game changer!", "Feeling inspired after reading this.", 
            "Great advice—thanks!", "What a creative approach!", "This has given me so much to think about.", "Completely agree with this sentiment.", "Thanks for putting this into words!", "This is such a fresh perspective!", "So true, couldn’t have said it better.", "I’m learning so much from this!", 
            "This post speaks to my soul.", "Wow, beautifully written!", "Do you mind explaining this a bit more?", "This just made my day better!", "Saving this for future reference!", "This is absolutely brilliant!", "Such an important point.", "Thanks for spreading positivity!", 
            "This deserves more attention!", "This was an eye-opener for me.", "So much wisdom in one post!", "I couldn’t stop nodding while reading this.", "This is so thought-provoking.", "What a lovely way to look at it.", "Completely agree—well said!", "This is the content I signed up for!", 
            "Feeling uplifted after reading this.", "I’m going to share this with my friends.", "Thank you for this beautiful insight.", "This makes so much sense.", "Appreciate you sharing this!", "This idea is worth exploring more.", "This hit me right in the feels!", "Absolutely spot on!", 
            "This gave me a new perspective.", "This is exactly what I needed to read.", "I can’t believe I didn’t think of this!", "What a gem of a post!", "Such a simple yet powerful idea.", "This post just brightened my day.", "Can’t wait to try this myself!", "Such an inspiring read.", 
            "This is pure gold—thank you!", "This concept is fascinating!", "This totally aligns with my thoughts.", "Love this approach to the topic.", "This has sparked so many ideas!", "Such a meaningful reminder.", "Thank you for this wonderful post.", "Wow, this hit home for me.", 
            "So beautifully articulated.", "This is wisdom at its finest.", "Thanks for shedding light on this topic.", "What a powerful perspective!", "This is truly inspiring!", "This resonates with me deeply.", "You’ve put my thoughts into words.", "Such a refreshing take on this!", 
            "This is the energy we need.", "This post deserves all the praise.", "Thank you for this incredible insight.", "This opened my eyes to something new.", "Such a profound statement.", "I couldn’t agree more—so true!", "This is a great way to look at it.", "This idea could change lives.", 
            "This made me think in a whole new way.", "I appreciate this thoughtful post.", "This really spoke to me today.", "Such a unique perspective!", "I’m so glad I came across this!", "This post feels like a warm hug."]

posts = ["This morning, I realized that small, consistent efforts really do lead to big changes. Progress isn’t always visible, but it’s happening. Stay patient and trust the process!",
"Every day might not be good, but there’s something good in every day. Let’s all try to focus on the little joys today.",
"Do you ever feel like you’re stuck in a loop, doing the same things over and over? Sometimes, all it takes is one small change to break free. What’s one thing you could change today?",
"Here’s a tip I’ve been using lately: whenever I feel overwhelmed, I make a quick list of the top three things I need to do. It helps me refocus and feel less stressed. Try it out!",
"Imagine waking up one year from now and realizing your life has completely transformed for the better. What’s the one thing you could start doing today to make that dream a reality?",
"I read a quote today that stuck with me: ‘It’s not about being the best; it’s about being better than you were yesterday.’ Progress over perfection, always!",
"Sometimes, you don’t need a plan. You just need to breathe, trust, and take the first step. The journey unfolds as you move forward. Keep going—you’re stronger than you think!",
"Have you ever noticed how a small act of kindness can completely change someone’s day? Let’s all try to spread a little extra positivity today. It’s contagious!",
"What if, instead of stressing about what’s next, we focused on what we can do with what we have right now? The present moment is powerful. Make the most of it!",
"Lately, I’ve been learning the importance of setting boundaries. It’s not selfish to prioritize your well-being—it’s necessary. Protecting your peace is the best form of self-care.",
"The other day, someone reminded me that failure isn’t the opposite of success; it’s part of the journey. Every setback is a setup for a comeback. Keep pushing forward!",
"Gratitude really does shift your perspective. Take a moment today to think of three things you’re thankful for. It’s a small habit that can have a big impact on your mindset.",
"Have you ever tried journaling your thoughts? It’s amazing how much clarity it brings. Writing things down helps you understand your feelings and see solutions more clearly.",
"Growth can be uncomfortable, but it’s necessary. If you’re feeling stretched right now, remember: diamonds are formed under pressure. You’re becoming something amazing!",
"Do one thing today that your future self will thank you for. Whether it’s a workout, a healthy meal, or just taking a moment to rest, small actions add up over time.",
"I heard someone say, ‘Don’t let perfect be the enemy of good.’ Sometimes, it’s better to start messy and refine as you go than to wait for the perfect moment. Just begin!",
"If you’re reading this, here’s your reminder to drink some water, take a deep breath, and stretch. Self-care doesn’t have to be complicated—it’s about the little things!",
"We’re often so focused on the finish line that we forget to enjoy the journey. Celebrate your small wins today—they’re all steps in the right direction.",
"Every challenge you face is an opportunity to grow. Life isn’t about avoiding struggles; it’s about learning and evolving through them. Embrace the process!",
"Have you ever paused to appreciate how far you’ve come? You’ve overcome challenges, grown, and learned so much. Celebrate your journey—you’re doing great!",
"Here’s a thought: What if today, you treated yourself with the same kindness and understanding you show to others? You deserve that same level of care and compassion.",
"Sometimes, the most productive thing you can do is rest. Recharging isn’t lazy—it’s essential. Take the time you need to come back stronger.",
"It’s amazing how much better things can feel after a deep breath and a quick pause. If you’re feeling overwhelmed, step back for a moment. Clarity often follows calm.",
"Dream big, but don’t forget to start small. Every big accomplishment begins with a single step. What’s one small action you can take today toward your goals?",
"We tend to overestimate what we can do in a day and underestimate what we can do in a year. Focus on consistency over intensity—it’s the key to long-term success!", 
"Here’s your friendly reminder: It’s okay to say no. Your time and energy are valuable. Don’t be afraid to protect your peace and prioritize what truly matters to you."]


def generate_users(names, last_names, quantity, _file):
    with open(_file, "w") as file:
        users_set = HashSet()
        for i in range(quantity):
            name, last_name = random.choice(names), random.choice(last_names)
            username = name + last_name[0]
            num = random.randint(100, 999)
            while username+str(num) in users_set:
                num = random.randint(100, 999)
            username += str(num)
            users_set.add(username)
            
            password = ""
            char = string.ascii_lowercase +string.digits
            for i in range(random.randint(8, 15)):
                password += random.choice(char)
            
            file.write(f"{username}|{name} {last_name}|{password}\n")
            
    return users_set


def generate_posts(users, posts, quantity, _file):
    posts_set = HashSet()
    with open(_file, "w") as file:
        for i in range(quantity):
            post_id = ""
            char = string.ascii_lowercase +string.digits
            for i in range(random.randint(10, 15)):
                post_id += random.choice(char)
                
            while post_id in posts_set:
                post_id = ""
                for i in range(random.randint(10, 15)):
                    post_id += random.choice(char)
                    
            posts_set.add(post_id)
            
            user = random.choice(list(users))
            content = random.choice(posts)
            
            file.write(f"{post_id}|{user}|{content}\n")
    return posts_set

def generate_comments(users_set, posts_set, quantity, _file):
    with open(_file, "w") as file:
        for i in range(quantity):
            user = random.choice(list(users_set))
            post = random.choice(list(posts_set))
            comment = random.choice(comments)
            file.write(f"{post}|{user}|{comment}\n")
            
def generate_likes(users_set, posts_set, _file):
    with open(_file, "w") as file:
        for post in posts_set:
            likes = HashSet()
            for i in range(random.randint(10, 100)):
                user = random.choice(list(users))
                if not user in likes:
                    likes.add(user)
                    file.write(f"{post}|{user}\n")
        
def generate_followers(users, _file):
    with open(_file, "w") as file:
        for i in users:
            followed = HashSet()
            for j in range(random.randint(20, 100)):
                user = random.choice(list(users))
                if user != i and not user in followed:
                        file.write(f"{i}|{user}\n")
                        followed.add(user)


if __name__ == "__main__":
    users = generate_users(names, last_names, 200, "users_database.txt")
    posts = generate_posts(users, posts, 600, "posts_database.txt")
    generate_comments(users, posts, 800, "comments_database.txt")
    generate_followers(users, "followers_database.txt")
    generate_likes(users, posts, "likes_database.txt")
    
    
    