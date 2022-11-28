class Todo:
    budget = 0
    tasks = []
    float_tasks = []
    bet_list = []

    def add(self, task):
        self.tasks.append(task)
        print(self.tasks)

    def delete(self, task):
        self.tasks.remove(task)
        print(self.tasks)

    def reset(self):
        self.tasks = []
        self.budget = 0
        self.float_tasks = []  
        self.bet_list = []    

    def get_tasks(self):
        return self.tasks

    def get_bet_list(self):
        return self.bet_list

    def gousei_odds(self):
        
        a = min(self.float_tasks)*100
        print(f"a: {a}")
        clist =  [a/x for x in self.float_tasks]
        print(f"clist: {clist}")
        c = sum(clist)
        print(f"c: {c}")
        d = a/c
        import math
        d = math.floor(d*100)/100

        gousei_odds=d
        
        return gousei_odds


    def get_dist_ratio(self):

        a = min(self.float_tasks)*100
        clist =  [a/x for x in self.float_tasks]
        c = sum(clist)
        
        for x in self.float_tasks:
            b = a/x
            bet = b/c * self.budget
            import math
            bet = math.floor(bet/100)*100
            self.bet_list.append(bet)

        print(self.bet_list)



    def float_henkan(self, budget):
        self.budget = int(budget)
        float_tasks = [float(x) for x in self.tasks]
        self.float_tasks = sorted(float_tasks)
        print(float_tasks)
        print(budget)
        gousei_odds = self.gousei_odds()
        print(gousei_odds)

        self.get_dist_ratio()

        return gousei_odds