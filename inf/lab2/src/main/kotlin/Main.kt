package ru.pozitp

import java.io.File

fun main() {
    // r1 r2 i1 r3 i2 i3 i4
    val intArr: MutableList<Int>
    while (true) {
        println("enter a message consisting of 7 digits 0 or 1, written without spaces:")
        val input = readln()
        if (input.length == 7 && Regex("[01]*").matches(input)) {
            intArr = input.map { it.toString().toInt() }.toMutableList()
            break
        } else {
            println("you must enter 7 bits containing only 0 and 1!")
        }
    }

    val s1 = (intArr[0] + intArr[2] + intArr[4] + intArr[6]) % 2
    val s2 = (intArr[1] + intArr[2] + intArr[5] + intArr[6]) % 2
    val s3 = (intArr[3] + intArr[4] + intArr[5] + intArr[6]) % 2

    val errPos = s1 + s2 * 2 + s3 * 4

    val bitType = when (errPos) {
        0 -> "correct"
        1 -> "r1"
        2 -> "r2"
        3 -> "i1"
        4 -> "r3"
        5 -> "i2"
        6 -> "i3"
        7 -> "i4"
        else -> "unknown"
    }
    println(bitType)

    File("result.txt").writeText(bitType)
}
