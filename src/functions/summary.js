const data = {
    "CHR": [
        {"judge": "hell", "grade": 0},
        {"min":1, "judge": "tortured", "grade": 0},
        {"min":2, "judge": "bad", "grade": 0},
        {"min":4, "judge": "ordinary", "grade": 0},
        {"min":7, "judge": "rare", "grade": 1},
        {"min":9, "judge": "epic", "grade": 2},
        {"min":11, "judge": "legendary", "grade": 3},
    ],
    "MNY": [
        {"judge": "hell", "grade": 0},
        {"min":1, "judge": "tortured", "grade": 0},
        {"min":2, "judge": "bad", "grade": 0},
        {"min":4, "judge": "ordinary", "grade": 0},
        {"min":7, "judge": "rare", "grade": 1},
        {"min":9, "judge": "epic", "grade": 2},
        {"min":11, "judge": "legendary", "grade": 3},
    ],
    "SPR": [
        {"judge": "hell", "grade": 0},
        {"min":1, "judge": "tortured", "grade": 0},
        {"min":2, "judge": "unlucky", "grade": 0},
        {"min":4, "judge": "ordinary", "grade": 0},
        {"min":7, "judge": "happy", "grade": 1},
        {"min":9, "judge": "blissed", "grade": 2},
        {"min":11, "judge": "destiny", "grade": 3},
    ],
    "INT": [
        {"judge": "hell", "grade": 0},
        {"min":1, "judge": "tortured", "grade": 0},
        {"min":2, "judge": "bad", "grade": 0},
        {"min":4, "judge": "ordinary", "grade": 0},
        {"min":7, "judge": "rare", "grade": 1},
        {"min":9, "judge": "epic", "grade": 2},
        {"min":11, "judge": "legendary", "grade": 3},
        {"min":21, "judge": "half god", "grade": 3},
        {"min":131, "judge": "god", "grade": 3},
    ],
    "STR": [
        {"judge": "hell", "grade": 0},
        {"min":1, "judge": "tortured", "grade": 0},
        {"min":2, "judge": "bad", "grade": 0},
        {"min":4, "judge": "ordinary", "grade": 0},
        {"min":7, "judge": "rare", "grade": 1},
        {"min":9, "judge": "epic", "grade": 2},
        {"min":11, "judge": "legendary", "grade": 3},
        {"min":21, "judge": "half god", "grade": 3},
        {"min":131, "judge": "god", "grade": 3},
    ],
    "AGE": [
        {"judge": "Stillborn", "grade": 0},
        {"min":1, "judge": "Die early", "grade": 0},
        {"min":10, "judge": "Juvenile", "grade": 0},
        {"min":18, "judge": "young age", "grade": 0},
        {"min":40, "judge": "Middle age", "grade": 0},
        {"min":60, "judge": "Sixtieth", "grade": 1},
        {"min":70, "judge": "Seventieth", "grade": 1},
        {"min":80, "judge": "Eightieth", "grade": 2},
        {"min":90, "judge": "Immortal", "grade": 2},
        {"min":100, "judge": "Eternal", "grade": 3},
    ],
    "SUM": [
        {"judge": "hell", "grade": 0},
        {"min":41, "judge": "tortured", "grade": 0},
        {"min":50, "judge": "bad", "grade": 0},
        {"min":60, "judge": "ordinary", "grade": 0},
        {"min":80, "judge": "rare", "grade": 1},
        {"min":100, "judge": "epic", "grade": 2},
        {"min":110, "judge": "legendary", "grade": 3},
        {"min":120, "judge": "Godlike", "grade": 3},
    ]
}

function summary(type, value) {
    let length = data[type].length;
    while(length--) {
        const {min, judge, grade} = data[type][length];
        if(min==void 0 || value >= min) return {judge, grade};
    }
}

export { summary };