package ch13;

import java.io.IOException;

import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.commons.beanutils.BeanUtils;

/**
 * 
 */
@WebServlet("/guestControl")
public class GuestController extends HttpServlet {
	private static final long serialVersionUID = 1L;
    private String id1="";
    
    GuestDAO dao;
	public void init(ServletConfig config) throws ServletException{
		super.init(config);
		dao=new GuestDAO();
	}
    /**
     * @see HttpServlet#HttpServlet()
     */
    public GuestController() {
        super();
        // TODO Auto-generated constructor stub
    }

    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		request.setCharacterEncoding("utf-8");
        String action=request.getParameter("action");
        String id=request.getParameter("id");
        if(id!=null) {
        	setID(id);
        }
        
        String view="";

        if(action==null) {
            getServletContext().getRequestDispatcher("/guestControl?action=list").forward(request, response);
    	}else{
            switch(action){
                case "list": view=list(request, response); break;
                case "insert": view=insert(request, response); break;
                case "list2": view=list2(request, response); break;
                case "list3": view=list3(request, response, getID()); break;
                case "update": view=update(request, response, getID()); break;
                
            }
            getServletContext().getRequestDispatcher("/ch13/"+view).forward(request, response);
        }
    }
    public String list(HttpServletRequest request, HttpServletResponse response) {
		request.setAttribute("guests", dao.getAll());
		return "guestInfo.jsp";
	}

	public String insert(HttpServletRequest request, HttpServletResponse response) {
		Guest s = new Guest();
		
		try{
			BeanUtils.populate(s, request.getParameterMap());
		} catch(Exception e){
			e.printStackTrace();
		}
		dao.insert(s);
		return list(request, response);
	}
	public String list2(HttpServletRequest request, HttpServletResponse response) {
		return "guestNew.jsp";
	}
	public String list3(HttpServletRequest request, HttpServletResponse response,String id) {
		request.setAttribute("guests1", dao.getRow(id));
		return "guestUpdate.jsp";
		
	}
	public void setID(String id) {
		this.id1=id;
	}
	public String getID() {
		return this.id1;
	}
    public String update(HttpServletRequest request, HttpServletResponse response, String id) {
		Guest s = new Guest();
		
		try{
			BeanUtils.populate(s, request.getParameterMap());
		} catch(Exception e){
			e.printStackTrace();
		}
		
		dao.update(s,id);
		return list(request, response);
	}

}
