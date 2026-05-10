class Twitter:

    def __init__(self):
        self.users = {} # userID: followerSet 
        self.tweetHeap = []
        heapq.heapify(self.tweetHeap)
        self.tweetCount = 0       

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetCount -= 1 # for the newest to be minimums
        if not userId in self.users:
            self.users[userId] = set()
            self.users[userId].add(userId)

        heapq.heappush(self.tweetHeap, [self.tweetCount, tweetId, userId])
        
    def getNewsFeed(self, userId: int) -> List[int]:
        if not userId in self.users:
            self.users[userId] = set()
            self.users[userId].add(userId)

        followers = self.users[userId]
        twtHeapCopy = self.tweetHeap[:]
        feed = []
        while len(feed) < 10 and twtHeapCopy:
            count, twtId, user = heapq.heappop(twtHeapCopy)
            if user in followers or user == userId:
                feed.append(twtId)

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.users:
            self.users[followerId] = set()
            self.users[followerId].add(followerId)

        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.users[followerId] and followerId != followeeId:
            self.users[followerId].discard(followeeId)
