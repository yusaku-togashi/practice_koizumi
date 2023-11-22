<!DOCTYPE html>
<html lang="ja" xmlns="http://www.w3.org/1999/html">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width-device-width, initial-scale=1">
<title><?php echo bloginfo('name'); ?></title>
<meta name="description" content="<?php bloginfo('description'); ?>">
<link rel="icon" href="<?php echo esc_url(get_theme_file_uri('img/favicon.ico')); ?>">
<link rel="stylesheet" href="<?php echo get_template_directory_uri(); ?>/assets/common/css/admin.css" />
<link rel="stylesheet" href="<?php echo get_template_directory_uri(); ?>/assets/common/css/base.css" />
<link rel="stylesheet" href="<?php echo get_template_directory_uri(); ?>/assets/common/css/layout.css" />
<link rel="stylesheet" href="<?php echo get_template_directory_uri(); ?>/assets/common/css/st_large.css" />
<link rel="stylesheet" href="<?php echo get_template_directory_uri(); ?>/assets/common/css/st_medium.css" />
<link rel="stylesheet" href="<?php echo get_template_directory_uri(); ?>/assets/common/css/st_small.css" />
<link rel="stylesheet" href="<?php echo get_template_directory_uri(); ?>/assets/common/css/sub.css" />

<script defer src="<?php echo get_template_directory_uri(); ?>/assets/common/js/fontsize.js">
<script defer src="<?php echo get_template_directory_uri(); ?>/assets/common/js/js/heightLine.js" type="text/javascript"></script>
<script defer src="<?php echo get_template_directory_uri(); ?>/assets/common/js/js/minmax.js" type="text/javascript"></script>
<script defer src="<?php echo get_template_directory_uri(); ?>/assets/common/js/open.js" type="text/javascript"></script>
<script defer src="<?php echo get_template_directory_uri(); ?>/assets/common/js/iepngfix.js" type="text/javascript"></script>
<script defer src="<?php echo get_template_directory_uri(); ?>/assets/common/js/smooth.pack.js" type="text/javascript"></script>
<script defer src="<?php echo get_template_directory_uri(); ?>/assets/common/js/styleswitcher.js" type="text/javascript"></script>
<?php wp_head(); ?>
</head>

<body>
    <header id="header" class="wrapper">
    <div id="global_header">
        <a name="top" id="top"></a>
        <div id="header_inner">
            <div id="logo">
                <h1><a href="./"><img src="<?php echo get_template_directory_uri(); ?>/assets/common/images/g_logo.gif" width="347" height="40" alt="株式会社コイズミ市場開発" /></a></h1>
            </div>
            <div id="header_info">
                <ul>
                    <li><a href="privacy.html"><img src="<?php echo get_template_directory_uri(); ?>/assets/common/images/bth_privacy.gif" alt="プライバシーポリシー" width="100" height="14" /></a></li>
                    <li class="none"><a href="sitemap.html"><img src="<?php echo get_template_directory_uri(); ?>/assets/common/images/bth_sitemap.gif" alt="サイトマップ" width="62" height="14" /></a></li>
                </ul>
            </div>
        </div>
        </div>

        <div id="global_nav">
            <ul>
                <li id="bt01" class="selected"><a href="/"><img src="<?php echo get_template_directory_uri(); ?>/assets/common/images/bt_01.gif" alt="トップページ" width="158" height="46" /></a></li>
                <li id="bt02" class="up"><a href="/company/"><img src="<?php echo get_template_directory_uri(); ?>/assets/common/images/bt_03.gif" alt="会社概要" width="158" height="46" /></a></li>
                <li id="bt03" class="up"><a href="/business/"><img src="<?php echo get_template_directory_uri(); ?>/assets/common/images/bt_04.gif" alt="事業内容" width="158" height="46" /></a></li>
                <li id="bt04" class="up"><a href="/work/"><img src="<?php echo get_template_directory_uri(); ?>/assets/common/images/bt_02.gif" alt="新規事業" width="158" height="46" /></a></li>
                <li id="bt05" class="up"><a href="/access/"><img src="<?php echo get_template_directory_uri(); ?>/assets/common/images/bt_05.gif" alt="アクセス" width="158" height="46" /></a></li>
                <li id="bt06" class="up end"><a href="/contact/"><img src="<?php echo get_template_directory_uri(); ?>/assets/common/images/bt_06.gif" alt="お問い合わせ" width="160" height="46" /></a></li>
            </ul>
        </div>
    </header>

