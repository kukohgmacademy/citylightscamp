document.addEventListener('DOMContentLoaded', () => {
    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Intersection Observer for scroll animations
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Optional: Stop observing once visible if you only want it to animate once
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Elements to observe
    const elementsToAnimate = document.querySelectorAll('.section-title, .card');
    elementsToAnimate.forEach(el => observer.observe(el));

    // TOC Toggle
    const tocHeader = document.querySelector('.toc-header');
    const tocContent = document.querySelector('.toc-content');
    if (tocHeader && tocContent) {
        tocHeader.addEventListener('click', () => {
            tocHeader.classList.toggle('open');
            tocContent.classList.toggle('open');
        });
    }

    // FAQ Accordion
    const faqQuestions = document.querySelectorAll('.faq-question');
    faqQuestions.forEach(question => {
        question.addEventListener('click', () => {
            const answer = question.nextElementSibling;

            // Toggle active class on question
            question.classList.toggle('active');

            // Toggle open class on answer
            if (answer.classList.contains('open')) {
                answer.classList.remove('open');
            } else {
                // Optional: Close other open answers
                document.querySelectorAll('.faq-answer').forEach(ans => ans.classList.remove('open'));
                document.querySelectorAll('.faq-question').forEach(q => q.classList.remove('active'));

                question.classList.add('active');
                answer.classList.add('open');
            }
        });
    });

    // Back to Top button
    const backToTopBtn = document.getElementById('backToTop');
    if (backToTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 500) {
                backToTopBtn.classList.add('show');
            } else {
                backToTopBtn.classList.remove('show');
            }
        });

        backToTopBtn.addEventListener('click', (e) => {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Mobile Menu Toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            // Toggle icon format
            const icon = menuToggle.querySelector('i');
            if (navLinks.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });

        // Close menu when a link is clicked
        const links = navLinks.querySelectorAll('a');
        links.forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                const icon = menuToggle.querySelector('i');
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            });
        });
    }
});
