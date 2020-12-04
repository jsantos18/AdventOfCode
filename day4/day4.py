import re

class passport:
    def __init__(self, current_passport_text, mode):
        self.current_passport_text = current_passport_text
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None
        self.birth(current_passport_text, mode)
        self.issue(current_passport_text, mode)
        self.expiration(current_passport_text, mode)
        self.height(current_passport_text, mode)
        self.hair_color(current_passport_text, mode)
        self.eye_color(current_passport_text, mode)
        self.passport_id(current_passport_text, mode)
        self.country_id(current_passport_text, mode)

    def birth(self, line, mode):
        if mode:
            birth_year = re.search(r'byr:([0-9]{4})\s', line)
        else:
            birth_year = re.search(r'byr:(\S+)', line)
        if birth_year != None:
            self.byr = birth_year.groups()[0]

    def issue(self, line, mode):
        if mode:
            issue_year = re.search(r'iyr:([0-9]{4})\s', line)
        else:
            issue_year = re.search(r'iyr:(\S+)', line)
        if issue_year != None:
            self.iyr = issue_year.groups()[0]

    def expiration(self, line, mode):
        if mode:
            expiration_year = re.search(r'eyr:([0-9]{4})\s', line)
        else:
            expiration_year = re.search(r'eyr:(\S+)', line)
        if expiration_year != None:
            self.eyr = expiration_year.groups()[0]
        
    def height(self, line, mode):
        if mode:
            hgt = re.search(r'hgt:([0-9]+(in|cm))\s', line)
        else:
            hgt = re.search(r'hgt:(\S+)', line)
        if hgt != None:
            self.hgt = hgt.groups()[0]

    def hair_color(self, line, mode):
        if mode:
            hcl = re.search(r'hcl:(\#[0-9a-fA-F]{6})\s', line)
        else:
            hcl = re.search(r'hcl:(\S+)', line)
        if hcl != None:
            self.hcl = hcl.groups()[0]

    def eye_color(self, line, mode):
        if mode:
            ecl = re.search(r'ecl:(|[a-zA-Z]{3})\s', line)
        else:
            ecl = re.search(r'ecl:(\S+)', line)
        if ecl != None:
            self.ecl = ecl.groups()[0]

    def passport_id(self, line, mode):
        if mode:
            pid = re.search(r'pid:([0-9]{9})\s', line)
        else:
            pid = re.search(r'pid:(\S+)', line)
        if pid != None:
            self.pid = pid.groups()[0]

    def country_id(self, line, mode):
        if mode:
            cid = re.search(r'cid:([0-9]{3})\s', line)
        else:
            cid = re.search(r'cid:(\S+)', line)
        if cid != None:
            self.cid = cid.groups()[0]
            
    def is_valid(self):
        if self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid:
            return True
        return False

    def valid_data(self):
        if self.is_valid():
            byr_valid = len(self.byr) <= 4 and 1920 <= int(self.byr) <= 2002
            iyr_valid = len(self.iyr) <= 4 and 2010 <= int(self.iyr) <= 2020
            eyr_valid = len(self.eyr) <= 4 and 2020 <= int(self.eyr) <= 2030
            hgt_valid = (self.hgt.endswith('cm') and 150 <= int(self.hgt[:-2]) <= 193) or (self.hgt.endswith("in") and 59 <= int(self.hgt[:-2]) <= 76)
            hcl_valid = re.match('^#[0-9a-f]{6}', self.hcl)
            ecl_valid = self.ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            pid_valid = len(self.pid) == 9 and self.pid.isdigit()

            return byr_valid and iyr_valid and eyr_valid and hgt_valid and hcl_valid and ecl_valid and pid_valid


    def to_string(self):
        print(self.current_passport_text)
        print(self.byr, self.iyr, self.eyr, self.hgt, self.hcl, self.ecl, self.pid)


if __name__ == "__main__":
    with open("day4/input.txt") as passports:
        passports_list = []
        valid_passport_list = []
        current_passport_text = ""
        for line in passports:
            if line == "\n":
                current_passport = passport(current_passport_text, False)
                if current_passport.is_valid():
                    passports_list.append(current_passport)
                if current_passport.valid_data():
                    valid_passport_list.append(current_passport)
                current_passport_text = ""
            else:
                current_passport_text += line
        print(len(passports_list), len(valid_passport_list))