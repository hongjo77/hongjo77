<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>방명록 목록</title>
<style>
body {
	font-family: Arial, sans-serif;
	background-color: #f7f7f7;
	margin: 0;
	padding: 0;
}

h1 {
	color: steelblue;
	text-align: center;
	margin-top: 0;
	padding-top: 10px;
	border-top: 1px solid #ccc;
}

h5 {
	text-align: right;
	padding: 5px;
}

table {
	border: 1px solid black;
	border-collapse: collapse;
	width: 100%;
}

th, td {
	text-align: center;
	padding: 8px;
}

th {
	background-color: #f7f7f7;
}

tr:nth-child(even) {
	background-color: #f9f9f9;
}

tr:hover {
	background-color: #ddd;
}

td {
	color: blue;
	font-size: 50px;
}

.container {
	display: flex;
	justify-content: center;
	align-items: center;
	height: 100vh;
}

button {	
	display: block;
	width: 100px;
	padding: 8px;
	font-size: 14px;
	font-weight: bold;
	color: #fff;
	background-color: #5cb85c;
	font-size: 15px;
	border: none;
	border-radius: 3px;
	cursor: pointer;
}

.form-container {
	background-color: #fff;
	border-radius: 5px;
	padding: 20px;
	box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
	max-height: 70vh;
	width: 50%; 
	margin: 0 auto;
}
</style>

<script>
	function callServlet() {
		window.location.href = "/jwbook/guestControl?action=list2";
	}
  
	function getUserName() {
		let table1 = document.getElementById('table1');

		for (let i = 1; i < table1.rows.length; i++) {
			table1.rows[i].cells[4].onclick = function () {
			let id = table1.rows[i].cells[0].innerText;
			window.location.href = "/jwbook/guestControl?id=" + id;
    	    window.location.href = "/jwbook/guestControl?action=list3";
     		}
		}
	}
</script>

</head>
<body>
	<div class="container">
		<div class="form-container">
			<h5>[<a href="/jwbook/guestControl">새로고침</a>]</h5>
			<h1>방명록 목록</h1>
			<hr>
				<table border="1" id="table1">
					<tr>
					<th>id</th>
					<th>이름</th>
					<th>이메일</th>
					<th>작성일</th>
					<th>제목</th>
				</tr>
			<c:forEach var="s" items="${guests}">
				<tr>
					<td>${s.id}</td>
					<td>${s.username}</td>
					<td>${s.email}</td>
					<td>${s.make}</td>
					<td onclick="getUserName()">${s.title}</td>
				</tr>
			</c:forEach>
				</table>
      <div class="container">
		<button type="button" onclick="callServlet()">등록</button>
	  </div>
	   </div>
	</div>
</body>
</html>