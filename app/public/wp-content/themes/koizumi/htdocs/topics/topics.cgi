#!/usr/bin/perl

#��������������������������������������������������������������������
#�� TopicsBoard v1.2 (2003/10/14)
#�� Copyright (c) KentWeb
#�� webmaster@kent-web.com
#�� http://www.kent-web.com/
#��������������������������������������������������������������������
$ver = 'TopicsBoard v1.2';
#��������������������������������������������������������������������
#�� [���ӎ���]
#�� 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����
#��    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B
#�� 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B
#��    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B
#�� 3. ���̃X�N���v�g�́Amethod=POST ��p�ł��B	
#��������������������������������������������������������������������

#------------#
#  ��{�ݒ�  #
#------------#

# �O���t�@�C����荞��
require './cgi-lib.pl';
require './jcode.pl';
require './topiset.cgi';

# �{�̃t�@�C��URL
$script = './topics.cgi';

# ���O�t�@�C��
$logfile = './topics.dat';

# �e���v���[�g
$tmpfile = './tmp.html';

# �Ǘ��p�X���[�h
$pass = 'koizumipass';

# �摜�f�B���N�g���Ƃ���URL
$imgdir = './img/';
$imgurl = 'http://www.koizumi-s.co.jp/';

# ���e�󗝍ő�T�C�Y (bytes)
# �� �� : 102400 = 100KB
$cgi_lib'maxdata = 307200;

# �摜�t�@�C���̍ő�\���̑傫���i�P�ʁF�s�N�Z���j
# �� ����𒴂���摜�͏k���\�����܂�
$MaxW = 200;	# ����
$MaxH = 120;	# �c��

# 1�y�[�W������\������
$pagelog = 50;

# �߂��URL
$home = '../index.html';

# URL�̎��������N (0=no 1=yes)
$autolink = 1;

# �ő�L����
# �� ����𒴂���L���͌Â����Ɏ����폜����܂�
$max = 100;

#------------#
#  �ݒ芮��  #
#------------#

&decode;
if ($mode eq "admin") { &admin; }
elsif ($mode eq "check") { &check; }
&logfile;

#------------#
#  �L���\��  #
#------------#
sub logfile {
	local($flag,$msg,$i,$next,$back,$loop,@head,@loop,@foot);

	# HTML�w�b�_
	print "Content-type: text/html\n\n";

	# �e���v���[�g�ǂݍ���
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

	# �f�[�^�ǂݍ���
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

		# URL�����N
		&auto_link($com) if ($autolink);

		$msg =~ s/!subject!/$sub/i;
		$msg =~ s/!date!/$date/i;
		$msg =~ s/!comment!/$com/i;

		# �摜
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

	# �y�[�W�J�z�{�^��
	$next = $page + $pagelog;
	$back = $page - $pagelog;
	if ($back >= 0) {
		$bflag=1;
		if ($pageBtn) {
			$backBtn = "<form action=\"$script\" method=get>\n";
			$backBtn .= "<input type=hidden name=page value=\"$back\">\n";
			$backBtn .= "<input type=submit value=\"$backForm\"></form>\n";
		} else {
			$backBtn = "<a href=\"$script?page=$back\"><img src=\"$backImg\" border=0 alt=\"�O�y�[�W\"></a>";
		}
	} else {
		$bflag=0;
		if ($pageBtn) { $backBtn = ""; }
		else { $backBtn = "<img src=\"$backImg\" alt=\"�O�y�[�W\">"; }
	}
	if ($next < $i) {
		$nflag=1;
		if ($pageBtn) {
			$nextBtn = "<form action=\"$script\" method=get>\n";
			$nextBtn .= "<input type=hidden name=page value=\"$next\">\n";
			$nextBtn .= "<input type=submit value=\"$nextForm\"></form>\n";
		} else {
			$nextBtn = "<a href=\"$script?page=$next\"><img src=\"$nextImg\" border=0 alt=\"���y�[�W\"></a>";
		}
	} else {
		$nflag=0;
		if ($pageBtn) { $nextBtn = ""; }
		else { $nextBtn = "<img src=\"$nextImg\" alt=\"���y�[�W\">"; }
	}

	# �w�b�_�\��
	foreach (@head) {
		s|!back!|$backBtn|;
		s|!next!|$nextBtn|;
		s|!home!|<a href="$home"><img src="$homeImg" border=0 alt="HOME�y�[�W"></a>|;

		if ($pageBtn) { s|!top!||; }
		else { s|!top!|<a href="$script"><img src="$topImg" border=0 alt="TOP�y�[�W"></a>|; }

		print;
	}

	print @loop;

	# �t�b�^�\��
	foreach (@foot) {
		s|!back!|$backBtn|;
		s|!next!|$nextBtn|;
		s|!home!|<a href="$home"><img src="$homeImg" border=0 alt="HOME�y�[�W"></a>|;

		if ($pageBtn) { s|!top!||; }
		else { s|!top!|<a href="$script"><img src="$topImg" border=0 alt="TOP�y�[�W"></a>|; }

		print;
	}
	exit;
}

#------------#
#  �Ǘ����  #
#------------#
sub admin {
	local($no,$dat,$sub,$com,$f,$del);

	# �F��
	if ($in{'pass'} ne $pass) { &error("�p�X���[�h���Ⴂ�܂�"); }

	# ���e�t�H�[��
	if ($in{'job'} eq "form") {

		&form;

	# ���e����
	} elsif ($in{'job'} eq "form2") {

		local($no,$t1,$w1,$h1,$t2,$w2,$h2,$t3,$w3,$h3,@file);

		if (!$in{'date'}) { &error("���t�������͂ł�"); }
		if (!$in{'comment'}) { &error("���b�Z�[�W�������͂ł�"); }

		# �^�O����
		if ($in{'tag'} == 1) {
			$in{'comment'} =~ s/<br>//g;
			$in{'comment'} = &tag($in{'comment'});
		}

		open(IN,"$logfile") || &error("Open Error: $logfile");
		@file = <IN>;
		close(IN);

		# �̔�
		($no) = split(/<>/, $file[0]);
		$no++;

		# �摜�A�b�v
		if ($in{'upfile1'} || $in{'upfile2'} || $in{'upfile3'}) {
			($t1,$w1,$h1,$t2,$w2,$h2,$t3,$w3,$h3) = &upload($no);
		}

		# �ő�L��������
		while ($max-1 <= @file) {
			$del = pop(@file);
			local($no,$date,$sub,$com,$t[0],$w[0],$h[0],
				$t[1],$w[1],$h[1],$t[2],$w[2],$h[2],$tag)
							= split(/<>/, $del);
			unlink("$imgdir$no-1$t[0]") if ($t[0]);
			unlink("$imgdir$no-2$t[1]") if ($t[1]);
			unlink("$imgdir$no-3$t[2]") if ($t[2]);
		}

		# �X�V
		unshift(@file,"$no<>$in{'date'}<>$in{'sub'}<>$in{'comment'}<>$t1<>$w1<>$h1<>$t2<>$w2<>$h2<>$t3<>$w3<>$h3<>$in{'tag'}\n");
		open(OUT,">$logfile") || &error("Write Error: $logfile");
		print OUT @file;
		close(OUT);

	# �폜
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

		# �X�V
		open(OUT,">$logfile") || &error("Write Error: $logfile");
		print OUT @new;
		close(OUT);

	# �C���t�H�[��
	} elsif ($in{'job'} eq "edit" && $in{'no'}) {

		local(@no) = split(/\0/, $in{'no'});

		open(IN,"$logfile") || &error("Open Error: $logfile");
		while (<IN>) {
			($no,$dat,$sub,$com,$t1,$w1,$h1,
				$t2,$w2,$h2,$t3,$w3,$h3,$tag) = split(/<>/);
			last if ($no[0] == $no);
		}
		close(IN);

		# �C�����
		&form($no,$dat,$sub,$com,$t1,$w1,$h1,$t2,$w2,$h2,$t3,$w3,$h3,$tag);

	# �C�����s
	} elsif ($in{'job'} eq "edit2" && $in{'no'}) {

		# �^�O����
		if ($in{'tag'} == 1) {
			$in{'comment'} =~ s/<br>//ig;
			$in{'comment'} = &tag($in{'comment'});
		}

		# �摜�A�b�v
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

		# �X�V
		open(OUT,">$logfile") || &error("Write Error: $logfile");
		print OUT @new;
		close(OUT);
	}

	&header;
	print <<"EOM";
<form action="$script">
<input type=submit value="�f���ɖ߂�"></form>
<ul>
<li>������I�����đ��M�{�^���������Ă��������B
</ul>
<form action="$script" method="POST">
<input type=hidden name=mode value="admin">
<input type=hidden name=pass value="$in{'pass'}">
�����F<select name=job>
<option value="edit">�C��
<option value="dele">�폜
</select>
<input type=submit value="���M����">
EOM

	# ���O�W�J
	open(IN,"$logfile") || &error("Open Error: $logfile");
	while (<IN>) {
		($no,$dat,$sub,$com,$t[0],$w[0],$h[0],
			$t[1],$w[1],$h[1],$t[2],$w[2],$h[2],$tag) = split(/<>/);

		$com =~ s/<([^>]|\n)*>//g;
		if (length($com) > 60) {
			$com = substr($com,0,60);
			$com .= "�E�E�E";
		}

		print "<hr><input type=checkbox name=no value=\"$no\"><b>$sub</b>";
		print "- $dat<br><span style='font-size:11px'>$com</span><br>\n";

		foreach $i (0 .. 2) {
			$j = $i + 1;
			next if (!$t[$i]);

			print "[<a href=\"$imgurl$no-$j$t[$i]\">�摜$j</a>]\n";
		}
	}
	close(IN);

	print "<hr></form>\n";
	print &HtmlBot;
	exit;
}

#----------------#
#  ���e�t�H�[��  #
#----------------#
sub form {
	local($no,$dat,$sub,$com,$t[0],$w[0],$h[0],
		$t[1],$w[1],$h[1],$t[2],$w[2],$h[2],$tag) = @_;

	if ($tag == 1) {
		# ���s�͂��̂܂�
		$com =~ s/<br>/<br>\r/ig;

		$checked = " checked";
	} else {
		# ���s�͕���
		$com =~ s/<br>/\r/ig;

		$checked = "";
	}

	# �p�����[�^��`
	local($job) = $in{'job'} . '2';

	# �V�K���e���͔N�������擾
	if ($dat eq "") {
		$ENV{'TZ'} = "JST-9";
		local($mday,$mon,$year) = (localtime(time))[3..5];
		$dat = sprintf("%04d/%02d/%02d", $year+1900,$mon+1,$mday);
	}

	# �t�H�[���\��
	&header;
	print <<"EOM";
<form>
<input type=button value="�O��ʂɖ߂�" onClick="history.back()">
</form>
<h1>�V����񓊍e�t�H�[��</h1>
<ul>
<li>HTML�^�O��L���ɂ���ꍇ�A�t�H�[�����̉��s�͖����ƂȂ邽�߁A
���s���镔���� &lt;br&gt; �ƋL�q���邱�ƁB
<li>�摜�̓Y�t�͔C�ӂł��B
</ul>
<form action="$script" method="POST" enctype="multipart/form-data">
<input type=hidden name=mode value="admin">
<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=job value="$job">
<input type=hidden name=no value="$no">
<table>
<tr>
  <td>�N����</td>
  <td><input type=text name=date value="$dat" size=30></td>
</tr>
<tr>
  <td>�{��</td>
  <td><input type=checkbox name=tag value="1"$checked>HTML�^�O�L�� (�A�����s�͖���)<br>
	<textarea name=comment cols=50 rows=6 wrap=soft>$com</textarea>
  </td>
</tr>
</table>
<p>
<input type=submit value="���M����">
</form>
EOM
	print &HtmlBot;
	exit;
}

#----------------#
#  �f�R�[�h����  #
#----------------#
sub decode {
	local($key,$val);

	&ReadParse;
	while ( ($key,$val) = each %in ) {

		if ($key !~ /^upfile/) {

			# �V�t�gJIS�R�[�h�ϊ�
			&jcode'convert(*val, 'sjis');

			# �^�O����
			$val =~ s/<>/&LT;&GT;/g;
			$val =~ s/&/&amp;/g;
			$val =~ s/"/&quot;/g;
			$val =~ s/</&lt;/g;
			$val =~ s/>/&gt;/g;

			# ���s����
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
#  HTML�w�b�_  #
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
#  �G���[����  #
#--------------#
sub error {
	&header;
	print <<"EOM";
<div align="center">
<h3>ERROR !</h3>
<font color="red">$_[0]</font>
<p>
<form>
<input type=button value="�O��ʂɖ߂�" onClick="history.back()">
</form>
</div>
EOM
	print &HtmlBot;
	exit;
}

#--------------------#
#  �摜�A�b�v���[�h  #
#--------------------#
sub upload {
	local($no) = @_;
	local($tail,$fnam,$macbin,$f,$i,$flag,$imgfile,
		$upfile,$length,$W,$H,$W2,$H2,@tail,@fnam,@name,@upfile);

	# �摜����
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

	# �t�@�C���`����F��
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

		# �A�b�v���[�h����
		if ($flag) { $f++; }
		else { push(@upfile,("","","")); next; }

		# �}�b�N�o�C�i���΍�
		if ($macbin) {
			$length = substr($upfile,83,4);
			$length = unpack("%N",$length);
			$upfile = substr($upfile,128,$length);
		}

		# �f�[�^������
		open(OUT,">$imgfile") || &error("�摜�A�b�v���s");
		binmode(OUT);
		binmode(STDOUT);
		print OUT $upfile;
		close(OUT);

		chmod (0666,$imgfile);

		# �摜�T�C�Y�擾
		if ($tail eq ".jpg") { ($W, $H) = &j_size($imgfile); }
		elsif ($tail eq ".gif") { ($W, $H) = &g_size($imgfile); }
		elsif ($tail eq ".png") { ($W, $H) = &p_size($imgfile); }

		# �摜�\���k��
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
#  JPEG�T�C�Y�F��  #
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
#  GIF�T�C�Y�F��  #
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
#  PNG�T�C�Y�F��  #
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
#  ����URL�����N  #
#-----------------#
sub auto_link {
	$_[0] =~ s/([^=^\"]|^)(https?\:[\w\.\~\-\/\?\&\+\=\:\@\%\;\#\%]+)/$1<a href=\"$2\" target=\"_blank\">$2<\/a>/g;
}

#------------#
#  �^�O����  #
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
#  �`�F�b�N���[�h  #
#------------------#
sub check {
	&header;
	print <<EOM;
<h2>Check Mode</h2>
<ul>
EOM

	# ���O�t�@�C��
	if (-e $logfile) {
		print "<li>���O�t�@�C���F�p�XOK!\n";
		if (-r $logfile && -w $logfile) { print "<li>���O�p�[�~�b�V�����FOK!\n"; }
		else { print "<li>���O�p�[�~�b�V�������s���ł��B\n"; }
	} else {
		print "<li>���O�t�@�C���̃p�X���s���ł��F $logfile\n";
	}

	# �摜�f�B���N�g��
	if (-d $imgdir) {
		print "<li>�摜�f�B���N�g���F�p�XOK!\n";
		if (-r $imgdir && -w $imgdir && -x $imgdir) {
			print "<li>�摜�f�B���N�g���̃p�[�~�b�V�����FOK!\n";
		} else {
			print "<li>�摜�f�B���N�g���̃p�[�~�b�V�������s���ł��B\n";
		}
	} else {
		print "<li>�摜�f�B���N�g���̃p�X���s���ł��F $imgdir\n";
	}

	print <<EOM;
<li>�o�[�W�����F$ver
</ul>

</body>
</html>
EOM
	exit;
}


__END__

