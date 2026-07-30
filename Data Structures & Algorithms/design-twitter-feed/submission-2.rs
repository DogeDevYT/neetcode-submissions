struct Twitter {
    count: i32,
    tweet_map: HashMap<i32, Vec<[i32; 2]>>,
    follow_map: HashMap<i32, HashSet<i32>>,
}

impl Twitter {
    fn new() -> Self {
        Twitter {
            count: 0,
            tweet_map: HashMap::new(),
            follow_map: HashMap::new(),
        }
    }

    fn post_tweet(&mut self, user_id: i32, tweet_id: i32) {
        let tweets = self.tweet_map.entry(user_id).or_default();
        tweets.push([self.count, tweet_id]);
        if tweets.len() > 10 {
            tweets.remove(0);
        }
        self.count -= 1;
    }

    fn get_news_feed(&mut self, user_id: i32) -> Vec<i32> {
        let mut res = Vec::new();
        self.follow_map
            .entry(user_id)
            .or_default()
            .insert(user_id);

        let followees: Vec<i32> = self
            .follow_map
            .get(&user_id)
            .cloned()
            .unwrap_or_default()
            .into_iter()
            .collect();

        // min-heap for final extraction
        let mut min_heap: BinaryHeap<std::cmp::Reverse<(i32, i32, i32, i32)>> =
            BinaryHeap::new();

        if followees.len() >= 10 {
            // Use a max-heap (BinaryHeap default) limited to size 10
            let mut max_heap: BinaryHeap<std::cmp::Reverse<(i32, i32, i32, i32)>> =
                BinaryHeap::new();
            for &f_id in &followees {
                if let Some(tweets) = self.tweet_map.get(&f_id) {
                    if !tweets.is_empty() {
                        let idx = tweets.len() - 1;
                        let t = tweets[idx];
                        max_heap
                            .push(std::cmp::Reverse((-t[0], t[1], f_id, idx as i32 - 1)));
                        if max_heap.len() > 10 {
                            max_heap.pop();
                        }
                    }
                }
            }
            while let Some(std::cmp::Reverse((neg_count, t_id, f_id, idx))) = max_heap.pop()
            {
                min_heap.push(std::cmp::Reverse((-neg_count, t_id, f_id, idx)));
            }
        } else {
            for &f_id in &followees {
                if let Some(tweets) = self.tweet_map.get(&f_id) {
                    if !tweets.is_empty() {
                        let idx = tweets.len() - 1;
                        let t = tweets[idx];
                        min_heap
                            .push(std::cmp::Reverse((t[0], t[1], f_id, idx as i32 - 1)));
                    }
                }
            }
        }

        while let Some(std::cmp::Reverse((_, t_id, f_id, idx))) = min_heap.pop() {
            if res.len() >= 10 {
                break;
            }
            res.push(t_id);
            if idx >= 0 {
                let tweets = &self.tweet_map[&f_id];
                let t = tweets[idx as usize];
                min_heap.push(std::cmp::Reverse((t[0], t[1], f_id, idx - 1)));
            }
        }
        res
    }

    fn follow(&mut self, follower_id: i32, followee_id: i32) {
        self.follow_map
            .entry(follower_id)
            .or_default()
            .insert(followee_id);
    }

    fn unfollow(&mut self, follower_id: i32, followee_id: i32) {
        if let Some(set) = self.follow_map.get_mut(&follower_id) {
            set.remove(&followee_id);
        }
    }
}