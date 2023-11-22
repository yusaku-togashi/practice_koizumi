#!/usr/bin/perl

#┌─────────────────────────────────
#│ TopicsBoard v1.2 (2003/10/14)
#│ Copyright (c) KentWeb
#│ webmaster@kent-web.com
#│ http://www.kent-web.com/
#└─────────────────────────────────
$ver = 'TopicsBoard v1.2';
#┌─────────────────────────────────
#│ [注意事項]
#│ 1. このスクリプトはフリーソフトです。このスクリプトを使用した
#│    いかなる損害に対して作者は一切の責任を負いません。
#│ 2. 設置に関する質問はサポート掲示板にお願いいたします。
#│    直接メールによる質問は一切お受けいたしておりません。
#│ 3. このスクリプトは、method=POST 専用です。	
#└─────────────────────────────────

#------------#
#  基本設定  #
#------------#

# 外部ファイル取り込み
require './cgi-lib.pl';
require './jcode.pl';
require './topiset.cgi';

# 本体ファイルURL
$script = './topics.cgi';

# ログファイル
$logfile = './topics.dat';

# テンプレート
$tmpfile = './tmp.html';

# 管理パスワード
$pass = 'koizumipass';

# 画像ディレクトリとそのURL
$imgdir = './img/';
$imgurl = 'http://www.koizumi-s.co.jp/';

# 投稿受理最大サイズ (bytes)
# → 例 : 102400 = 100KB
$cgi_lib'maxdata = 307200;

# 画像ファイルの最大表示の大きさ（単位：ピクセル）
# → これを超える画像は縮小表示します
$MaxW = 200;	# 横幅
$MaxH = 120;	# 縦幅

# 1ページあたり表示件数
$pagelog = 50;

# 戻り先URL
$home = '../index.html';

# URLの自動リンク (0=no 1=yes)
$autolink = 1;

# 最大記事数
# → これを超える記事は古い順に自動削除されます
$max = 100;

#------------#
#  設定完了  #
#------------#

&decode;
if ($mode eq "admin") { &admin; }
elsif ($mode eq "check") { &check; }
&logfile;

#------------#
#  記事表示  #
#------------#
sub logfile {
	local($flag,$msg,$i,$next,$back,$loop,@head,@loop,@foot);

	# HTMLヘッダ
	print "Content-type: text/html\n\n";

	# テンプレート読み込み
	$loop="";
	@head=();
	@foot=();
	$flag=0;
	open(IN,"$tmpfile") || &error("Open Error: $tmpfile");
	while (<IN>) {
		push(@head,$_) if (!$flag);

		if (/<!-- line1 -->/) { $flag=1; }
		elsif (/<!-- line2 -->/) { $flag=2; }
		if ($flag == 1) { s/\n//g; $loop .= $_; }
		elsif ($flag == 2) { push(@foot,$_); }
	}
	close(IN);

	# データ読み込み
	@loop=();
	$i=0;
	open(IN,"$logfile") || &error("Open Error: $logfile");
	while (<IN>) {
		$i++;
		next if ($i < $page + 1);
		next if ($i > $page + $pagelog);

		$msg = $loop;
		($no,$date,$sub,$com,$t[0],$w[0],$h[0],
			$t[1],$w[1],$h[1],$t[2],$w[2],$h[2]) = split(/<>/);

		# URLリンク
		&auto_link($com) if ($autolink);

		$msg =~ s/!subject!/$sub/i;
		$msg =~ s/!date!/$date/i;
		$msg =~ s/!comment!/$com/i;

		# 画像
		foreach $i (0 .. 2) {
			$j = $i + 1;
			$image = "!image-$j\!";

			if (!$t[$i]) { $msg =~ s/$image//i; next; }

			if ($h[$i] && $w[$i]) { $wh = "width=$w[$i] height=$h[$i]"; }
			else { $wh=""; }

			$msg =~ s|$image|<a href=\"$imgurl$no-$j$t[$i]\" target=\"_blank\"><img src=\"$imgurl$no-$j$t[$i]\" border=0 align=top $wh></a>|i;
		}

		push(@loop,$msg);
	}
	close(IN);

	# ページ繰越ボタン
	$next = $page + $pagelog;
	$back = $page - $pagelog;
	if ($back >= 0) {
		$bflag=1;
		if ($pageBtn) {
			$backBtn = "<form action=\"$script\" method=get>\n";
			$backBtn .= "<input type=hidden name=page value=\"$back\">\n";
			$backBtn .= "<input type=submit value=\"$backForm\"></form>\n";
		} else {
			$backBtn = "<a href=\"$script?page=$back\"><img src=\"$backImg\" border=0 alt=\"前ページ\"></a>";
		}
	} else {
		$bflag=0;
		if ($pageBtn) { $backBtn = ""; }
		else { $backBtn = "<img src=\"$backImg\" alt=\"前ページ\">"; }
	}
	if ($next < $i) {
		$nflag=1;
		if ($pageBtn) {
			$nextBtn = "<form action=\"$script\" method=get>\n";
			$nextBtn .= "<input type=hidden name=page value=\"$next\">\n";
			$nextBtn .= "<input type=submit value=\"$nextForm\"></form>\n";
		} else {
			$nextBtn = "<a href=\"$script?page=$next\"><img src=\"$nextImg\" border=0 alt=\"次ページ\"></a>";
		}
	} else {
		$nflag=0;
		if ($pageBtn) { $nextBtn = ""; }
		else { $nextBtn = "<img src=\"$nextImg\" alt=\"次ページ\">"; }
	}

	# ヘッダ表示
	foreach (@head) {
		s|!back!|$backBtn|;
		s|!next!|$nextBtn|;
		s|!home!|<a href="$home"><img src="$homeImg" border=0 alt="HOMEページ"></a>|;

		if ($pageBtn) { s|!top!||; }
		else { s|!top!|<a href="$script"><img src="$topImg" border=0 alt="TOPページ"></a>|; }

		print;
	}

	print @loop;

	# フッタ表示
	foreach (@foot) {
		s|!back!|$backBtn|;
		s|!next!|$nextBtn|;
		s|!home!|<a href="$home"><img src="$homeImg" border=0 alt="HOMEページ"></a>|;

		if ($pageBtn) { s|!top!||; }
		else { s|!top!|<a href="$script"><img src="$topImg" border=0 alt="TOPページ"></a>|; }

		print;
	}
	exit;
}

#------------#
#  管理画面  #
#------------#
sub admin {
	local($no,$dat,$sub,$com,$f,$del);

	# 認証
	if ($in{'pass'} ne $pass) { &error("パスワードが違います"); }

	# 投稿フォーム
	if ($in{'job'} eq "form") {

		&form;

	# 投稿処理
	} elsif ($in{'job'} eq "form2") {

		local($no,$t1,$w1,$h1,$t2,$w2,$h2,$t3,$w3,$h3,@file);

		if (!$in{'date'}) { &error("日付が未入力です"); }
		if (!$in{'comment'}) { &error("メッセージが未入力です"); }

		# タグ復元
		if ($in{'tag'} == 1) {
			$in{'comment'} =~ s/<br>//g;
			$in{'comment'} = &tag($in{'comment'});
		}

		open(IN,"$logfile") || &error("Open Error: $logfile");
		@file = <IN>;
		close(IN);

		# 採番
		($no) = split(/<>/, $file[0]);
		$no++;

		# 画像アップ
		if ($in{'upfile1'} || $in{'upfile2'} || $in{'upfile3'}) {
			($t1,$w1,$h1,$t2,$w2,$h2,$t3,$w3,$h3) = &upload($no);
		}

		# 最大記事数調整
		while ($max-1 <= @file) {
			$del = pop(@file);
			local($no,$date,$sub,$com,$t[0],$w[0],$h[0],
				$t[1],$w[1],$h[1],$t[2],$w[2],$h[2],$tag)
							= split(/<>/, $del);
			unlink("$imgdir$no-1$t[0]") if ($t[0]);
			unlink("$imgdir$no-2$t[1]") if ($t[1]);
			unlink("$imgdir$no-3$t[2]") if ($t[2]);
		}

		# 更新
		unshift(@file,"$no<>$in{'date'}<>$in{'sub'}<>$in{'comment'}<>$t1<>$w1<>$h1<>$t2<>$w2<>$h2<>$t3<>$w3<>$h3<>$in{'tag'}\n");
		open(OUT,">$logfile") || &error("Write Error: $logfile");
		print OUT @file;
		close(OUT);

	# 削除
	} elsif ($in{'job'} eq "dele" && $in{'no'}) {

		local($i,$j,$f);
		local(@new)=();
		open(IN,"$logfile") || &error("Open Error: $logfile");
		while (<IN>) {
			$f=0;
			($no,$date,$sub,$com,$t[0],$w[0],$h[0],
				$t[1],$w[1],$h[1],$t[2],$w[2],$h[2],$tag) = split(/<>/);

			foreach $del ( split(/\0/, $in{'no'}) ) {
				if ($no == $del) {
					$f++;
					foreach $i (0 .. 2) {
						$j = $i+1;
						unlink("$imgdir$no-$j$t[$i]");
					}
					last;
				}
			}
			if (!$f) { push(@new,$_); }
		}
		close(IN);

		# 更新
		open(OUT,">$logfile") || &error("Write Error: $logfile");
		print OUT @new;
		close(OUT);

	# 修正フォーム
	} elsif ($in{'job'} eq "edit" && $in{'no'}) {

		local(@no) = split(/\0/, $in{'no'});

		open(IN,"$logfile") || &error("Open Error: $logfile");
		while (<IN>) {
			($no,$dat,$sub,$com,$t1,$w1,$h1,
				$t2,$w2,$h2,$t3,$w3,$h3,$tag) = split(/<>/);
			last if ($no[0] == $no);
		}
		close(IN);

		# 修正画面
		&form($no,$dat,$sub,$com,$t1,$w1,$h1,$t2,$w2,$h2,$t3,$w3,$h3,$tag);

	# 修正実行
	} elsif ($in{'job'} eq "edit2" && $in{'no'}) {

		# タグ復元
		if ($in{'tag'} == 1) {
			$in{'comment'} =~ s/<br>//ig;
			$in{'comment'} = &tag($in{'comment'});
		}

		# 画像アップ
		if ($in{'upfile1'} || $in{'upfile2'} || $in{'upfile3'}) {
			($t1,$w1,$h1,$t2,$w2,$h2,$t3,$w3,$h3) = &upload($in{'no'});
		}

		local(@new)=();
		open(IN,"$logfile") || &error("Open Error: $logfile");
		while (<IN>) {
			s/\n$//;
			($no,$dat,$sub,$com,$t01,$w01,$h01,
				$t02,$w02,$h02,$t03,$w03,$h03,$tag) = split(/<>/);

			if ($in{'no'} == $no) {

				if ($in{'del1'}) {
					unlink("$imgdir$no-1$t01");
					$t01 = $w01 = $h01 = "";
				}
				if ($in{'del2'}) {
					unlink("$imgdir$no-2$t02");
					$t02 = $w02 = $h02 = "";
				}
				if ($in{'del3'}) {
					unlink("$imgdir$no-3$t03");
					$t03 = $w03 = $h03 = "";
				}
				if ($t1) { $t01=$t1; $w01=$w1; $h01=$h1; }
				if ($t2) { $t02=$t2; $w02=$w2; $h02=$h2; }
				if ($t3) { $t03=$t3; $w03=$w3; $h03=$h3; }

				$_ = "$no<>$in{'date'}<>$in{'sub'}<>$in{'comment'}<>$t01<>$w01<>$h01<>$t02<>$w02<>$h02<>$t03<>$w03<>$h03<>$in{'tag'}<>";
			}
			push(@new,"$_\n");
		}
		close(IN);

		# 更新
		open(OUT,">$logfile") || &error("Write Error: $logfile");
		print OUT @new;
		close(OUT);
	}

	&header;
	print <<"EOM";
<form action="$script">
<input type=submit value="掲示板に戻る"></form>
<ul>
<li>処理を選択して送信ボタンを押してください。
</ul>
<form action="$script" method="POST">
<input type=hidden name=mode value="admin">
<input type=hidden name=pass value="$in{'pass'}">
処理：<select name=job>
<option value="edit">修正
<option value="dele">削除
</select>
<input type=submit value="送信する">
EOM

	# ログ展開
	open(IN,"$logfile") || &error("Open Error: $logfile");
	while (<IN>) {
		($no,$dat,$sub,$com,$t[0],$w[0],$h[0],
			$t[1],$w[1],$h[1],$t[2],$w[2],$h[2],$tag) = split(/<>/);

		$com =~ s/<([^>]|\n)*>//g;
		if (length($com) > 60) {
			$com = substr($com,0,60);
			$com .= "・・・";
		}

		print "<hr><input type=checkbox name=no value=\"$no\"><b>$sub</b>";
		print "- $dat<br><span style='font-size:11px'>$com</span><br>\n";

		foreach $i (0 .. 2) {
			$j = $i + 1;
			next if (!$t[$i]);

			print "[<a href=\"$imgurl$no-$j$t[$i]\">画像$j</a>]\n";
		}
	}
	close(IN);

	print "<hr></form>\n";
	print &HtmlBot;
	exit;
}

#----------------#
#  投稿フォーム  #
#----------------#
sub form {
	local($no,$dat,$sub,$com,$t[0],$w[0],$h[0],
		$t[1],$w[1],$h[1],$t[2],$w[2],$h[2],$tag) = @_;

	if ($tag == 1) {
		# 改行はそのまま
		$com =~ s/<br>/<br>\r/ig;

		$checked = " checked";
	} else {
		# 改行は復元
		$com =~ s/<br>/\r/ig;

		$checked = "";
	}

	# パラメータ定義
	local($job) = $in{'job'} . '2';

	# 新規投稿時は年月日を取得
	if ($dat eq "") {
		$ENV{'TZ'} = "JST-9";
		local($mday,$mon,$year) = (localtime(time))[3..5];
		$dat = sprintf("%04d/%02d/%02d", $year+1900,$mon+1,$mday);
	}

	# フォーム表示
	&header;
	print <<"EOM";
<form>
<input type=button value="前画面に戻る" onClick="history.back()">
</form>
<h1>新着情報投稿フォーム</h1>
<ul>
<li>HTMLタグを有効にする場合、フォーム内の改行は無効となるため、
改行する部分で &lt;br&gt; と記述すること。
<li>画像の添付は任意です。
</ul>
<form action="$script" method="POST" enctype="multipart/form-data">
<input type=hidden name=mode value="admin">
<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=job value="$job">
<input type=hidden name=no value="$no">
<table>
<tr>
  <td>年月日</td>
  <td><input type=text name=date value="$dat" size=30></td>
</tr>
<tr>
  <td>本文</td>
  <td><input type=checkbox name=tag value="1"$checked>HTMLタグ有効 (但し改行は無効)<br>
	<textarea name=comment cols=50 rows=6 wrap=soft>$com</textarea>
  </td>
</tr>
</table>
<p>
<input type=submit value="送信する">
</form>
EOM
	print &HtmlBot;
	exit;
}

#----------------#
#  デコード処理  #
#----------------#
sub decode {
	local($key,$val);

	&ReadParse;
	while ( ($key,$val) = each %in ) {

		if ($key !~ /^upfile/) {

			# シフトJISコード変換
			&jcode'convert(*val, 'sjis');

			# タグ処理
			$val =~ s/<>/&LT;&GT;/g;
			$val =~ s/&/&amp;/g;
			$val =~ s/"/&quot;/g;
			$val =~ s/</&lt;/g;
			$val =~ s/>/&gt;/g;

			# 改行処理
			if ($key eq "comment") {
				$val =~ s/\r\n/<br>/g;
				$val =~ s/\r/<br>/g;
				$val =~ s/\n/<br>/g;
			} else {
				$val =~ s/\r//g;
				$val =~ s/\n//g;
			}
		}
		$in{$key} = $val;
	}
	$mode = $in{'mode'};
	$page = $in{'page'};
}

#--------------#
#  HTMLヘッダ  #
#--------------#
sub header {
	if ($headflag) { return; }

	print "Content-type: text/html\n\n";
	print <<"EOM";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="ja">
<head>
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=Shift_JIS">
<title>$ver</title></head>
<body bgcolor="#f0f0f0" text="#000000">
EOM
	$headflag=1;
}

#--------------#
#  エラー処理  #
#--------------#
sub error {
	&header;
	print <<"EOM";
<div align="center">
<h3>ERROR !</h3>
<font color="red">$_[0]</font>
<p>
<form>
<input type=button value="前画面に戻る" onClick="history.back()">
</form>
</div>
EOM
	print &HtmlBot;
	exit;
}

#--------------------#
#  画像アップロード  #
#--------------------#
sub upload {
	local($no) = @_;
	local($tail,$fnam,$macbin,$f,$i,$flag,$imgfile,
		$upfile,$length,$W,$H,$W2,$H2,@tail,@fnam,@name,@upfile);

	# 画像処理
	$macbin=0;
	@tail=();
	@fnam=();
	@name=();
	foreach (@in) {
		if (/(.*)Content-type:(.*)/i) {
			$tail = $2;
			$tail =~ s/\r//g;
			$tail =~ s/\n//g;
			push(@tail,$tail);
		}
		if (/.*name=\"(.*)\";.*filename=\"(.*)\"/i) {
			$fnam = $2;
			$fnam =~ s/\r//g;
			$fnam =~ s/\n//g;
			push(@fnam,$fnam);
			push(@name,$1);
		}
		if (/application\/x-macbinary/i) { $macbin=1; }
	}

	# ファイル形式を認識
	$f=0;
	$i=0;
	@upfile=();
	foreach (0 .. $#tail) {
		$i++;
		$flag=0;
		if ($tail[$_] =~ /image\/gif/i) { $tail=".gif"; $flag=1; }
		elsif ($tail[$_] =~ /image\/jpeg/i) { $tail=".jpg"; $flag=1; }
		elsif ($tail[$_] =~ /image\/x-png/i) { $tail=".png"; $flag=1; }
		if (!$flag) {
			if ($fnam[$_] =~ /\.gif$/i) { $tail=".gif"; $flag=1; }
			elsif ($fnam[$_] =~ /\.jpe?g$/i) { $tail=".jpg"; $flag=1; }
			elsif ($fnam[$_] =~ /\.png$/i) { $tail=".png"; $flag=1; }
		}

		if ($name[$_] eq "upfile$i") {
			$upfile = $in{"upfile$i"};
			$imgfile = "$imgdir/$no-$i$tail";
		}

		# アップロード結果
		if ($flag) { $f++; }
		else { push(@upfile,("","","")); next; }

		# マックバイナリ対策
		if ($macbin) {
			$length = substr($upfile,83,4);
			$length = unpack("%N",$length);
			$upfile = substr($upfile,128,$length);
		}

		# データ書込み
		open(OUT,">$imgfile") || &error("画像アップ失敗");
		binmode(OUT);
		binmode(STDOUT);
		print OUT $upfile;
		close(OUT);

		chmod (0666,$imgfile);

		# 画像サイズ取得
		if ($tail eq ".jpg") { ($W, $H) = &j_size($imgfile); }
		elsif ($tail eq ".gif") { ($W, $H) = &g_size($imgfile); }
		elsif ($tail eq ".png") { ($W, $H) = &p_size($imgfile); }

		# 画像表示縮小
		if ($W > $MaxW || $H > $MaxH) {
			$W2 = $MaxW / $W;
			$H2 = $MaxH / $H;
			if ($W2 < $H2) { $key = $W2; }
			else { $key = $H2; }
			$W = int ($W * $key) || 1;
			$H = int ($H * $key) || 1;
		}
		push(@upfile,($tail,$W,$H));
	}
	return @upfile;
}

#------------------#
#  JPEGサイズ認識  #
#------------------#
sub j_size {
	local($jpeg) = @_;
	local($t, $m, $c, $l, $W, $H);

	open(JPEG, "$jpeg") || return (0,0);
	binmode JPEG;
	read(JPEG, $t, 2);
	while (1) {
		read(JPEG, $t, 4);
		($m, $c, $l) = unpack("a a n", $t);

		if ($m ne "\xFF") {
			$W = $H = 0;
			last;
		} elsif ((ord($c) >= 0xC0) && (ord($c) <= 0xC3)) {
			read(JPEG, $t, 5);
			($H, $W) = unpack("xnn", $t);
			last;
		} else {
			read(JPEG, $t, ($l - 2));
		}
	}
	close(JPEG);
	return ($W, $H);
}

#-----------------#
#  GIFサイズ認識  #
#-----------------#
sub g_size {
	local($gif) = @_;
	local($data);

	open(GIF,"$gif") || return (0,0);
	binmode(GIF);
	sysread(GIF,$data,10);
	close(GIF);

	if ($data =~ /^GIF/) { $data = substr($data,-4); }

	$W = unpack("v",substr($data,0,2));
	$H = unpack("v",substr($data,2,2));
	return ($W, $H);
}

#-----------------#
#  PNGサイズ認識  #
#-----------------#
sub p_size {
	local($png) = @_;
	local($data);

	open(PNG, "$png") || return (0,0);
	binmode(PNG);
	read(PNG, $data, 24);
	close(PNG);

	$W = unpack("N", substr($data, 16, 20));
	$H = unpack("N", substr($data, 20, 24));
	return ($W, $H);
}

#-----------------#
#  自動URLリンク  #
#-----------------#
sub auto_link {
	$_[0] =~ s/([^=^\"]|^)(https?\:[\w\.\~\-\/\?\&\+\=\:\@\%\;\#\%]+)/$1<a href=\"$2\" target=\"_blank\">$2<\/a>/g;
}

#------------#
#  タグ復元  #
#------------#
sub tag {
	local($_) = @_;

	s/&lt;/</g;
	s/&gt;/>/g;
	s/&amp;/&/g;
	s/&quot;/"/g;
	$_;
}

#------------------#
#  チェックモード  #
#------------------#
sub check {
	&header;
	print <<EOM;
<h2>Check Mode</h2>
<ul>
EOM

	# ログファイル
	if (-e $logfile) {
		print "<li>ログファイル：パスOK!\n";
		if (-r $logfile && -w $logfile) { print "<li>ログパーミッション：OK!\n"; }
		else { print "<li>ログパーミッションが不正です。\n"; }
	} else {
		print "<li>ログファイルのパスが不正です： $logfile\n";
	}

	# 画像ディレクトリ
	if (-d $imgdir) {
		print "<li>画像ディレクトリ：パスOK!\n";
		if (-r $imgdir && -w $imgdir && -x $imgdir) {
			print "<li>画像ディレクトリのパーミッション：OK!\n";
		} else {
			print "<li>画像ディレクトリのパーミッションが不正です。\n";
		}
	} else {
		print "<li>画像ディレクトリのパスが不正です： $imgdir\n";
	}

	print <<EOM;
<li>バージョン：$ver
</ul>

</body>
</html>
EOM
	exit;
}


__END__

