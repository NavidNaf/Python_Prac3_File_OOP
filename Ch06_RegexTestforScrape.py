import re

testString = """
 <div class="book-cover">

					 <a href="http://dimik.pub/book/525/java-web-programing-by-anm-bazlur-rahman"><img src="http://dimik.pub/wp-content/uploads/2020/02/javaWeb.jpg"></a>
                </div><!-- end .book-cover -->



                <div class="slide-description">

                    <div class="inner-sd">

                        <div class="top-sd-head clearfix">

                            <div class="tsh-left">

                            <h2 class="sd-title"><a href="http://dimik.pub/book/525/java-web-programing-by-anm-bazlur-rahman">জাভা ওয়েব প্রোগ্রামিং</a></h2>

                            </div><!-- end .tsh-left -->
"""
regexPattern = re.findall(
    r'<div class="book-cover">\s*<a href="(.*?)">\s*<img src="(.*?)">.*?<h2 class="sd-title"><.*?>(.*?)<', testString, re.S)

print(regexPattern)
