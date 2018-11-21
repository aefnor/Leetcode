var mostOccuringCharInString = function (s) {
    var count = 0;
    var tempChar = ''
    var isBiggest = 0
    for (var i = 0; i < s.length; i++) {
        // console.log("Inside the for loop", s[i])
        // console.log("============================================================")
        if(tempChar !== s[i]){
            tempChar = s[i]
            // console.log("\t Char does not match the previous!", tempChar)
        }
        if (tempChar === s[i-1]) {
            count++;
            // console.log("\t Char does match the previous!", count)
        }
        else {
            if (count >= isBiggest) {
                isBiggest = count
                // console.log("\tThe number is bigger than the previous count!", isBiggest)
            }
            else {
                // console.log("\tReset to 0!")
                count = 0
            }
        }
        // console.log("\n")
    }
    console.log(isBiggest)
    // return isBiggest
};

mostOccuringCharInString("ABCAAAABBC")
mostOccuringCharInString("abcsssssssssddsssssddddd")
// mostOccuringCharInString("FFFFFFFFFFFFAAAAAAAAAAAAAAA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!@@@@@FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")