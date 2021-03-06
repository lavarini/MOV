<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"[]>
<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr" lang="en-US" xml:lang="en">
    <head>

        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <title>Home</title>



        <link rel="stylesheet" href="style.css" type="text/css" media="screen" />
        <!--[if IE 6]><link rel="stylesheet" href="style.ie6.css" type="text/css" media="screen" /><![endif]-->
        <!--[if IE 7]><link rel="stylesheet" href="style.ie7.css" type="text/css" media="screen" /><![endif]-->

        <script type="text/javascript" src="jquery.js"></script>
        <script type="text/javascript" src="script.js"></script>
		<script type="text/javascript" src="js.js"></script>

    </head>
    <body>
		<div class="login" style="display:none">
			<input name="email" id="email" value="" />
			<input name="senha" id="senha" value="" type="password"/>
			<input id="logar" type="button" value="Login"/>
		</div>
        <div id="main">
            <div class="cleared reset-box"></div>
            <div class="bar nav">
                <div class="nav-outer">
                    <div class="nav-wrapper">
                        <div class="nav-inner">
                            <?php include('menu.php'); ?>
                        </div>
                    </div>
                </div>
            </div>
            <div class="cleared reset-box"></div>
            <div class="box sheet">
                <div class="box-body sheet-body">
                    <div class="layout-wrapper">
                        <div class="content-layout">
                            <div class="content-layout-row">
                                <div class="layout-cell content">
                                    <div class="box post">
                                        <div class="box-body post-body">
                                            <div class="post-inner article">
                                                <h2 class="postheader">
                                                    
                                                </h2>
                                                <div class="postcontent">
                                                    
                                                </div>
                                                <div class="cleared"></div>
                                            </div>

                                            <div class="cleared"></div>
                                        </div>
                                    </div>

                                    <div class="cleared"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="cleared"></div>

                    <div class="cleared"></div>
                </div>
            </div>
            <div class="footer">
                <div class="footer-body">
                    <div class="footer-center">
                        <div class="footer-wrapper">
                            <div class="footer-text">
                                <p>Copyright © 2012, PAS/UNI-BH. All Rights Reserved.</p>
                                <div class="cleared"></div>
                                <p class="page-footer"></p>
                            </div>
                        </div>
                    </div>
                    <div class="cleared"></div>
                </div>
            </div>
            <div class="cleared"></div>
        </div>

    </body>
</html>
