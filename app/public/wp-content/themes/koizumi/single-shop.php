 <?php get_header('shop'); ?>

 <main class="single">
  <h1 class="shop-detail-title">
    店舗詳細
  </h1>
 
  <?php while ( have_posts() ) : the_post(); ?>

  <?php $terms = get_the_terms($post->ID, 'shop'); ?>

  <article>
        <?php $shopImage = get_field('shop_image');
          if( !empty( $shopImage ) ): ?>
          <img class="shop-detail-image" src="<?php echo esc_url($shopImage['url']); ?>" alt="<?php echo esc_attr($profileImage['alt']); ?>" />
        <?php endif; ?>
      <h1 class="ttl"><?php the_title(); ?></h1>
      <time datetime="<?php the_time( 'Y-m-d' )?>"><?php the_time( 'Y.m.d' ); ?></time>
      <dd><?php the_field('shop_adress'); ?></dd>

      <div class="edit-area">
        <?php the_content(); ?>
      </div>
    </article>
  <?php endwhile; ?>
 </main>

 <?php get_footer(); ?>