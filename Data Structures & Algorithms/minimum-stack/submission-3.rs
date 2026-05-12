struct MinStack {
    min_val: i64,
    stack: Vec<i64>
}

impl MinStack {
    pub fn new() -> Self {
        Self {
            min_val: 0,
            stack: Vec::new(),
        }
    }

    pub fn push(&mut self, val: i32) {
        let val = val as i64;
        if self.stack.is_empty() 
        {
            self.stack.push(0);
            self.min_val = val;
        } else 
        {
            self.stack.push(val - self.min_val);
            if val < self.min_val {
                self.min_val = val;
            }
        }
    }

    pub fn pop(&mut self) {
        if let Some(top) = self.stack.pop() 
        {
            if top < 0 
            {
                self.min_val -= top;
            }
        }
    }

    pub fn top(&self) -> i32 {
        let top = *self.stack.last().unwrap();
        if top > 0 
        {
            (top + self.min_val) as i32
        } else 
        {
            self.min_val as i32
        }
    }

    pub fn get_min(&self) -> i32 {
        self.min_val as i32
    }
}
