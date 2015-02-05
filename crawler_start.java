package crawl;
import java.io.IOException;

import org.jsoup.*;
import org.jsoup.helper.*;
import org.jsoup.nodes.*;
import org.jsoup.select.*;

public class start {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		Document doc = Jsoup.connect("http://en.wikipedia.org/").get();
		Elements newsHeadlines = doc.select("#mp-itn b a");
		System.out.println(doc);
	}

}
