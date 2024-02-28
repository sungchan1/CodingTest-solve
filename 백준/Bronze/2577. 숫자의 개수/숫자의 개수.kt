@file:JvmName("JDoodle")
fun main(args: Array<String>) {
  val a = readln().toInt()
  val b = readln().toInt()
  val c = readln().toInt()
  
  val sumOf = (a*b*c).toString()
  
  for (i in 0..9){
    println("${sumOf.count { it ==  '0' + i }}")
    }
 }