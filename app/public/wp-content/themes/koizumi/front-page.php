<?php get_header(); ?>

<main>
    <div id="visual">
        <img src="<?php echo get_template_directory_uri(); ?>/assets/common/images/g_main.jpg" alt="グローバルな思考と明るい未来への広がり、そして、実りある価値の創造" width="950" height="320" />
    </div>

    <div id="contents">
        <div id="main">

            <div class="box1">
                <h2 class="bar"><span>御挨拶</span></h2>
                <p>私たち(株)コイズミ市場開発は、経営ビジョンに<br>
                「お客様第一」「品質第一」の理念を掲げております。<br>
                お客様と共に新しいビジネスを創造し、社会貢献する為の<br>
                「価値創造パートナー」としてお役に立てるよう努力してまいります。</p>
            </div>
            <?php $the_query = new WP_Query( array( 'post_type' => 'post', 'posts_per_page' => -1 ) ); ?>
            <?php if ( $the_query->have_posts() ) : ?>
            <div class="archive-box">
                <h4 class="archive-title">新着情報</h3>
                <div class="news">
                    <dl>
                        <?php query_posts('showposts=5'); ?>
                        <?php if(have_posts()) : while(have_posts()) : the_post(); ?>
                        <div class="news-item">
                            <a href="<?php the_permalink(); ?>">
                                <dt><span class="date"><?php the_time( 'Y年m月d日' ); ?></span></dt>
                                <dd><strong><?php the_title(); ?></strong></dd>
                                <dd><?php the_field('products_information'); ?></dd>
                            </a>
                        </div>
                        <?php endwhile; endif; ?>
                    </dl>
                    <?php wp_reset_postdata(); ?>
	            </div>
            </div>
            <?php endif; ?>

            <?php $shop_query = new WP_Query( array('post_type' => 'shop', 'posts_per_page' => 5,
             'tax_query' => array(
                array(
                    'taxonomy' => 'kyoten', 
                    'field'    => 'slug', 
                    'terms'    => array( 'abroad' ),
                ),),) ); ?>
            <div class="shop-block">
            <h3>店舗情報</h3>
                <dl>
                    <?php if ($shop_query->have_posts()) :while ($shop_query->have_posts()) : $shop_query->the_post(); ?>
                        <div class="shop-item">
                            <?php $shopImage = get_field('shop_image');
                            if( !empty( $shopImage ) ): ?>
                            <img src="<?php echo esc_url($shopImage['url']); ?>" alt="<?php echo esc_attr($profileImage['alt']); ?>" />
                            <?php endif; ?>
                            <a href="<?php the_permalink(); ?>">
                                <dt><?php the_title('<h2>', '</h2>'); ?></dt>
                                <dd><?php the_field('shop_category'); ?></dd>
                                <dd><?php the_field('shop_adress'); ?></dd>
                            </a>
                        </div>
                        <?php endwhile; endif; ?>
                </dl>
                <a class="shop-archive-btn" href="/shop">店舗一覧ページへ</a>
            </div>
            <?php wp_reset_postdata(); ?>


            <ul class="cbox">
                <li class="leftbox">
                    <h3><a href="company.html">会社概要</a></h3>
                    <p>コイズミ市場開発会社概要</p>
                    <ul>
                        <li><a href="company.html">会社概要</a></li>
                        <li><a href="history.html">沿革</a></li>
                        <li><a href="business.html">事業内容</a></li>
                    </ul>
                </li>
                <li class="rightbox">
                    <h3><a href="work/">新規事業</a></h3>
                    <ul>
                        <li><a href="work/energy_saving/">省エネ事業</a></li>
                        <li><a href="work/binder/">特殊シリカバインダー</a></li>
                        <li><a href="work/dermal/">皮膚紋理検出剤</a></li>
                    </ul>
                </li>
            </ul>
            <ul class="cbox">
                <li class="leftbox">
                    <h3><a href="access.html">アクセス</a></h3>
                    <p>会社までのアクセス方法</p>
                    <ul>
                        <li><a href="access.html">アクセス方法</a></li>
                    </ul>
                </li>
                <li class="rightbox">
                    <h3><a href="contact.html">お問い合わせ</a></h3>
                    <p>各種お問い合わせ窓口</p>
                    <ul>
                        <li><a href="contact.html">お問い合わせフォーム</a></li>
                    </ul>
                </li>
            </ul>
        </div>

        <div id="sub">
            <ul id="fontbox">
                <li id="stx"><img src="<?php echo get_template_directory_uri(); ?>/assets/common/images/tx_font.gif" alt="文字サイズ変更" width="82" height="18" /></li>
                <li id="ss"><a href="javascript:void(0);" onclick="setActiveStyleSheet('small'); return false;"><img src="<?php echo get_template_directory_uri(); ?>/assets/common/images/tx_s.gif" alt="小" width="24" height="18" /></a></li>
                <li id="mm"><a href="javascript:void(0);" onclick="setActiveStyleSheet('medium'); return false;"><img src="<?php echo get_template_directory_uri(); ?>/assets/common/images/tx_m.gif" alt="中" width="24" height="18" /></a></li>
                <li id="ll"><a href="javascript:void(0);" onclick="setActiveStyleSheet('large'); return false;"><img src="<?php echo get_template_directory_uri(); ?>/assets/common/images/tx_l.gif" alt="大" width="24" height="18" /></a></li>
            </ul>
            <h3 class="mgb10"><a href="contact.html"><img src="<?php echo get_template_directory_uri(); ?>/assets/common/images/baner_contact.gif" width="230" height="81" alt="お問い合わせ" /></a></h3>
            <h3><img src="<?php echo get_template_directory_uri(); ?>/assets/common/images/st_info.gif" alt="株式会社コイズミ市場開発" width="230" height="36" /></h3>
            <div class="sub_box">
                <div class="dot">
                    <p>〒101-0047<br />
                    東京都千代田区内神田2-6-11<br />
                    若松ビル 5F<br /></p>
                    <span class="detail"><a href="access.html">詳しいアクセス方法</a></span>
                </div>

                <ul id="stelfax">
                    <li><img src="<?php echo get_template_directory_uri(); ?>/assets/common/images/g_tel.gif" alt="TEL:03-3256-3466" width="204" height="27" /></li>
                    <li><img src="<?php echo get_template_directory_uri(); ?>/assets/common/images/g_fax.gif" alt="FAX:03-3256-3468" width="204" height="27" /></li>
                </ul>
            </div>

            <div id="youtube"><iframe width="230" height="129" src="https://www.youtube.com/embed/HUFPLOK9EqQ" frameborder="0" allowfullscreen></iframe></div>

        </div>
    </div>
</main>

<?php get_footer(); ?>