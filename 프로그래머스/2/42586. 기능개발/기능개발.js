function solution(progresses, speeds) {
    var answer = [];
    var days = [];
    
    for (let i = 0; i<progresses.length ; i++){
        var day = Math.floor((100 - progresses[i]) / speeds[i]);

        if ((100 - progresses[i]) % speeds[i] !== 0) {
            day += 1;
        }
        days.push(day)
    }
    
    var current_day = days[0]
    count = 0
    
    for (let i = 0; i<days.length; i++){
        if (days[i] <= current_day){
            count += 1
        } else{
            answer.push(count)
            current_day = days[i]
            count = 1
        }
    }
    answer.push(count)
    
    return answer;
}