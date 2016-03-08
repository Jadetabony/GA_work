class Introduction(object):
    class_names = {}

    def __init__(self, name, job, origin, hobby1, hobby2, fun_fact):
        self.name=name
        self.job = job
        self.origin = origin
        self.hobby1 = hobby1
        self.hobby2 = hobby2
        self.fun_fact= fun_fact


    def add_name(self):
        if not self.name in Introduction.class_names:
            print self.name, "has not been introduced!"
            Introduction.class_names[self.name] = "not introduced"
        else:
            print self.name, "has been introduced."

    def print_intro(self):
        self.job = self.job.lower()
        if self.job[0] in ('a', 'e', 'i', 'o', 'u'):
            print "Hi! I'm %s!  I'm an %s and I'm orignially from %s." %(self.name, self.job, self.origin)
            print "When not programming, I like %s and %s." %(self.hobby1, self.hobby2)
            print self.fun_fact
            Introduction.class_names[self.name] = "introduced"
        else:
            print "Hi! I'm %s!  I'm a %s and I'm orignially from %s." %(self.name, self.job, self.origin),
            print "When not programming, I like %s and %s." %(self.hobby1, self.hobby2)
            print self.fun_fact
            Introduction.class_names[self.name] = "introduced"


jade.print_intro()

jade.add_name()
