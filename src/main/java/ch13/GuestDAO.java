package ch13;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

public class GuestDAO {
    Connection conn=null;
    PreparedStatement pstmt;

    final String JDBC_DRIVER = "org.h2.Driver";
    final String JDBC_URL="jdbc:h2:tcp://localhost/~/jwbookdb";

    public void open(){
        try{
            Class.forName(JDBC_DRIVER);
            conn = DriverManager.getConnection(JDBC_URL,"jwbook","7789");
        } catch(Exception e){
            e.printStackTrace();
        }
    }
    public void close(){
        try{
            pstmt.close();
            conn.close();
        } catch(Exception e){
            e.printStackTrace();
        }
    }
    public void insert(Guest s){
        open();
        String sql = "insert into guestbook(username, email, make, title , content) values(?,?,?,?,?)";
        try{
           
            pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, s.getUsername());
            pstmt.setString(2, s.getEmail());
            pstmt.setString(3, s.getMake());
            pstmt.setString(4, s.getTitle());
            pstmt.setString(5, s.getContent());
            pstmt.executeUpdate();
        } catch(Exception e){
            e.printStackTrace();
        } finally{
            close();
        }
    }
    public void update(Guest s,String id){
        open();
        String sql = "update guestbook set username=? , email=?, make=?, title=? , content=? where id="+id;
        
        try{           
        	pstmt = conn.prepareStatement(sql);
        	pstmt.setString(1, s.getUsername());
            pstmt.setString(2, s.getEmail());
            pstmt.setString(3, s.getMake());
            pstmt.setString(4, s.getTitle());
            pstmt.setString(5, s.getContent());
            pstmt.executeUpdate();
        } catch(Exception e){
            e.printStackTrace();
        } finally{
            close();
        }
    }
    public List<Guest> getAll(){
        open();
        List<Guest> guests = new ArrayList<>();

        try{
            pstmt=conn.prepareStatement("select * from guestbook order by 1 desc");
            ResultSet rs = pstmt.executeQuery();
            while(rs.next()){
                Guest s = new Guest();
                s.setId(rs.getInt("id"));
                s.setUsername(rs.getString("username"));
                s.setEmail(rs.getString("email"));
                LocalDate now=java.time.LocalDate.now();
                DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
                String formatedNow = now.format(formatter);
                s.setMake(formatedNow);
                s.setTitle(rs.getString("title"));
                s.setContent(rs.getString("content"));
                guests.add(s);
            } 
        }catch(Exception e){
                e.printStackTrace();
            } finally{
                close();
            }
        return guests;
    }
    public List<Guest> getRow(String id){
        open();
        List<Guest> guests1 = new ArrayList<>();
        System.out.println(id);
        try{
            pstmt=conn.prepareStatement("select * from guestbook where id="+id);
            ResultSet rs = pstmt.executeQuery();
            
            while(rs.next()){
            	Guest s = new Guest();
                s.setId(rs.getInt("id"));
                s.setUsername(rs.getString("username"));
                s.setEmail(rs.getString("email"));
                s.setMake(rs.getString("make"));
                s.setTitle(rs.getString("title"));
                s.setContent(rs.getString("content"));
                guests1.add(s);
            }
        }catch(Exception e){
                e.printStackTrace();
            } finally{
                close();
            }
        return guests1;
    }
}

