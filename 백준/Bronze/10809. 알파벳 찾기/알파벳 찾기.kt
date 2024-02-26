@file:JvmName("JDoodle")
fun main(args: Array<String>) {
  var input = readln() 
  
  for (i in 'a' .. 'z'){
    print("${input.indexOf(i)} ")
  }
  
}