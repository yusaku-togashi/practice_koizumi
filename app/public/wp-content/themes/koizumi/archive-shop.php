 <?php get_header('shop'); ?>

 <main class="archive">
 <div class="shop">
  <h4>店舗一覧</h4>
  <?php
  $paged = get_query_var('paged') ? get_query_var('paged') : 1;
  $args = array(
    'post_type' => array('shop'),
    'paged' => $paged,
    'posts_per_page' => 4,

  );

  $wp_query = new WP_Query($args);

    $wp_query->query($args);
    if ($wp_query->have_posts()) : while ($wp_query->have_posts()) : $wp_query->the_post();
        $obj = get_post_type_object($post->post_type);?>
    <dl class="archive-shop-item">
        <dt class="post-date"><?php the_time('Y-m-d'); ?></dt>
        <dd class="shop-title">
            <a href="<?php the_permalink(); ?>">
                <?php the_title(); ?>
            </a>
        </dd>
    </dl>
    <?php endwhile;
    
    endif;
    wp_reset_postdata();
    ?>
    <?php the_posts_pagination(
      array(
        'mid_size'      => 1, 
        'prev_next'     => true, 
        'prev_text'     => ('<'), 
        'next_text'     => ('>'), 
        'type'          => 'list', 
      )
); ?>
</div>
 </main>

 <?php get_footer(); ?>