@file:JvmName("JDoodle")
fun main(args: Array<String>) {
  
  var remain: Int
  val remains = mutableSetOf<Int>()
  for (i in 1..10){
    remain = readln().toInt() % 42
    remains.add(remain)
  }
  
  print(remains.size)
}