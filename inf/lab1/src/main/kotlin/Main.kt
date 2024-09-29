package ru.pozitp

fun convertFibToDec(str: String): Long {
    var temp1 = 0
    var temp2 = 1
    var result: Long = 0
    for (i in 1..str.length) {
        result += temp1 * str[str.length - i].toString().toLong()

        val sum = temp1 + temp2
        temp1 = temp2
        temp2 = sum
    }

    return result
}

fun main(array: Array<String>) {
    if (array.isEmpty() || array.size > 1 || !Regex("[01]*").matches(array[0])) {
        println("You must provide one number in fibonacci numerical system!")
        return
    }

    println(convertFibToDec(array[0]))
}
