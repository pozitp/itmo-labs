package ru.pozitp

fun main(args: Array<String>) {
    // r1 r2 i1 r3 i2 i3 i4
    if (args.size != 1 || !Regex("[01]*").matches(args[0])) {
        println("You should provide 7 bits and it should contain only 0 and 1!")
        return
    }
    val charArr = args[0].toCharArray()
    val intArr = charArr.map { it.toString().toInt() }.toIntArray()

    val s1 = (intArr[0] + intArr[2] + intArr[4] + intArr[6]) % 2
    val s2 = (intArr[1] + intArr[2] + intArr[5] + intArr[6]) % 2
    val s3 = (intArr[3] + intArr[4] + intArr[5] + intArr[6]) % 2

    val errPos = s1 + s2 * 2 + s3 * 4
    if (errPos == 0) {
        println("No errors")
    } else {
        println("Error in position $errPos")
        intArr[errPos - 1] = intArr[errPos - 1] xor 1
        println("Corrected message: ${intArr.joinToString("")}")
    }
}
