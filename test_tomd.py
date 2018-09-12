import tomd
from tomd import Tomd

string = """
<h1>h1</h1>
<h2>h2</h2>
<h3>h3</h3>
<h4>h4</h4>
<h5>h5</h5>
<h6>h6</h6>
<p>paragraph
<a href="https://github.com">link</a>
<img src="https://github.com" class="dsad">img</img>
<img src="https://github.com" class="dsad"/>
<img src="https://github.com" class="dsad">
</p>
<ul>
<li>1</li>
<li>2</li>
<li>3</li>
</ul>
<ol>
<li>1</li>
<li>2</li>
<li>3</li>
</ol>
<blockquote>blockquote</blockquote>
<p><code>inline code</code></p>
<pre><code>block code</code></pre>
<p>
<del>del</del>
<b>bold</b>
<i>italic</i>
<b><i>bold italic</i></b>
<em>em</em>
<strong>strong</strong>
aa <strong> strong   </strong> aa
</p>

<hr/>

<table>
<thead>
<tr class="1">
<th>th1</th>
<th>th2</th>
</tr>
</thead>
<tbody>
<tr>
<td>td</td>
<td>td</td>
</tr>
<tr>
<td>td</td>
<td>td</td>
</tr></tbody></table>
<div>
<p><span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-1-Frame" tabindex="0" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><msup><mn>2</mn><mi>n</mi></msup></math>" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-1" style="width: 1.146em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.917em; height: 0px; font-size: 125%;"><span style="position: absolute; clip: rect(1.489em, 1000.92em, 2.574em, -999.997em); top: -2.397em; left: 0em;"><span class="mrow" id="MathJax-Span-2"><span class="msubsup" id="MathJax-Span-3"><span style="display: inline-block; position: relative; width: 0.917em; height: 0px;"><span style="position: absolute; clip: rect(3.146em, 1000.46em, 4.174em, -999.997em); top: -3.997em; left: 0em;"><span class="mn" id="MathJax-Span-4" style="font-family: STIXGeneral-Regular;">2</span><span style="display: inline-block; width: 0px; height: 4.003em;"></span></span><span style="position: absolute; top: -4.397em; left: 0.517em;"><span class="mi" id="MathJax-Span-5" style="font-size: 70.7%; font-family: STIXGeneral-Italic;">n</span><span style="display: inline-block; width: 0px; height: 4.003em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.403em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.068em; border-left: 0px solid; width: 0px; height: 1.075em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>n</mi></msup></math></span></span>
<script type="math/tex" id="MathJax-Element-1">2^n</script></p>
<p><span class="MathJax_Preview" style="color: inherit; display: none;"></span><div class="MathJax_Display" style="text-align: center;"><span class="MathJax" id="MathJax-Element-2-Frame" tabindex="0" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot; display=&quot;block&quot;><mi>a</mi><mo>=</mo><mi>b</mi></math>" role="presentation" style="text-align: center; position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-6" style="width: 2.902em; display: inline-block;"><span style="display: inline-block; position: relative; width: 2.302em; height: 0px; font-size: 125%;"><span style="position: absolute; clip: rect(1.702em, 1002.25em, 2.702em, -999.998em); top: -2.548em; left: 0em;"><span class="mrow" id="MathJax-Span-7"><span class="mi" id="MathJax-Span-8" style="font-family: STIXGeneral-Italic;">a</span><span class="mo" id="MathJax-Span-9" style="font-family: STIXGeneral-Regular; padding-left: 0.302em;">=</span><span class="mi" id="MathJax-Span-10" style="font-family: STIXGeneral-Italic; padding-left: 0.302em;">b</span></span><span style="display: inline-block; width: 0px; height: 2.552em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.059em; border-left: 0px solid; width: 0px; height: 1.003em;"></span></span></nobr><span class="MJX_Assistive_MathML MJX_Assistive_MathML_Block" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mi>a</mi><mo>=</mo><mi>b</mi></math></span></span></div>
<script type="math/tex; mode=display" id="MathJax-Element-2">a=b</script></p>
</div>
"""

print(Tomd(string).markdown)
print(tomd.convert(string))
