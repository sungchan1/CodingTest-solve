@file:JvmName("JDoodle")
fun main(args: Array<String>) {
  
  val remains = mutableSetOf<Int>()
  for (i in 1..10){
    remains.add(readln().toInt() % 42)
  }
 
  print(remains.size)
}