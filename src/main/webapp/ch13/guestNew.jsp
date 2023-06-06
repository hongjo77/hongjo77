<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>방명록 입력</title>
<style>
body {
	font-family: Arial, sans-serif;
	background-color: #f7f7f7;
	margin: 0;
	padding: 0;
}

.container {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	height: 100vh;
}

.form-container {
	background-color: #fff;
	border-radius: 5px;
	padding: 20px;
	box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
	max-width: 500px; 
}

h2 {
	color: steelblue;
	text-align: center;
	margin-top: 0;
	padding-top: 10px;
	border-top: 1px solid #ccc;
}

.form-group {
	margin-bottom: 15px;
}

label {
	display: block;
	font-weight: bold;
}

input[type="text"],
input[type="password"] {
 	 width: 100%;
	padding: 8px;
	font-size: 14px;
	border: 1px solid #ccc;
	border-radius: 3px;
	box-sizing: border-box;
}

input[type="text"]:focus,
input[type="password"]:focus {
	outline: none;
	border-color: #00FF00;
	box-shadow: 0 0 5px rgba(102, 175, 233, 0.5);
}

button {
	display: block;
	width: 100%;
	padding: 8px;
	font-size: 14px;
	font-weight: bold;
	color: #fff;
	background-color: #00FF00;
	border: none;
	border-radius: 3px;
	cursor: pointer;
}

button[type="button"] {
	background-color: #808080;
}

button[type="submit"] {
	background-color: #5cb85c;
}

button[type="button"],
button[type="submit"] {
	margin-top: 10px;
}
</style>

<script>
function input() {
	var username = document.getElementById("username").value;
	var email = document.getElementById("email").value;
	var title = document.getElementById("title").value;
	var passwd = document.getElementById("passwd").value;
	var content = document.getElementById("content").value;

	if (username === "" || email === "" || title === "" || passwd === "" || content === "") {
		alert("빈칸을 모두 채워주세요");
		return false;
	}

	document.getElementById('frm').submit();
	return true;
}
	
function cancel() {
	document.getElementById("username").value = "";
	document.getElementById("email").value = "";
    document.getElementById("title").value = "";
    document.getElementById("passwd").value = "";
    document.getElementById("content").value = "";
}

function callServlet() {
    window.location.href = "/jwbook/guestControl?action=list";
}

</script>
</head>
<body>
  <div class="container">
    <div class="form-container">
      <h2>방명록 입력</h2>
      <form id="frm" method="post" action="/jwbook/guestControl?action=insert" onsubmit="return input();">
        <div class="form-group">
          <label for="username">이름</label>
          <input id="username" type="text" name="username"><br>
        </div>
        <div class="form-group">
          <label for="email">이메일</label>
          <input id="email" type="text" name="email"><br>
        </div>
        <div class="form-group">
          <label for="title">제목</label>
          <input id="title" type="text" name="title"><br>
        </div>
        <div class="form-group">
          <label for="passwd">비밀번호</label>
          <input id="passwd" type="password" name="passwd"><br>
        </div>
        <div class="form-group">
          <label for="content">내용</label>
          <input id="content" type="text" size="100" maxlength="50" name="content"><br>
        </div>
        <button type="submit" onclick="input()">입력</button>
      </form>
      <button type="button" onclick="cancel()">취소</button>
      <button type="button" onclick="callServlet()">목록</button>
    </div>
  </div>
</body>
</html>