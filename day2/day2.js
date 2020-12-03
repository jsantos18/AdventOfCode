const fs = require('fs')

let parse = (line) => {
    amounts = line.match('([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)')
    return amounts
}

let search = (least, most, character, string) => {
    let char_amount = 0
    for (var i = 0; i < string.length; i++) {
        if (string[i] == character) {
            char_amount++
        }
    }
    if (parseInt(least) <= char_amount && char_amount <= parseInt(most)) return 1
    return 0
}

let positions = (pos1, pos2, character, string) => {
    first_pos = string[parseInt(pos1) - 1] == character
    second_pos = string[parseInt(pos2) - 1] == character
    if (first_pos ^ second_pos) return 1
    return 0
}

fs.readFile('day2/input.txt', function(err, data) {
    if (err) return;
    var lines = data.toString().split('\n')
    var valid_passwords_1 = 0
    var valid_passwords_2 = 0
    for (var i = 0; i < lines.length; i++) {
        var matched = parse(lines[i])
        valid_passwords_1 += search(matched[1], matched[2], matched[3], matched[4])
        valid_passwords_2 += positions(matched[1], matched[2], matched[3], matched[4])
    }
    console.log("Valid Passwords 1: ", valid_passwords_1)
    console.log("Valid Passwords 2: ", valid_passwords_2)
})